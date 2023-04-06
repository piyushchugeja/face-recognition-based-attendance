import openpyxl 
import smtplib
from datetime import datetime
from prettytable import PrettyTable
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
path = "Attendance.xlsx"

def get_dict():
    wb_obj = openpyxl.load_workbook(path)
    sheet = wb_obj['Details']
    data = {}
    for row in sheet.rows:
        for values in row:
            data[values.row] = [values.value for values in row]
    return data

def add_column():
    today = datetime.date(datetime.now())
    curr_month = today.strftime("%B")
    wb_obj = openpyxl.load_workbook(path) 
    try:
        sheet_obj = wb_obj[curr_month]
    except:
        wb_obj.create_sheet(curr_month)
        sheet_obj = wb_obj[curr_month]
        sheet_obj.cell(row=1, column=1).value = 'Roll no'
        sheet_obj.cell(row=1, column=2).value = 'Name'
        sheet_2 = wb_obj['Details']
        for i in range(2, sheet_2.max_row+1):
            sheet_obj.cell(row=i, column=1).value = sheet_2.cell(row=i, column=1).value
            sheet_obj.cell(row=i, column=2).value = sheet_2.cell(row=i, column=2).value
        wb_obj.save(path)
    last = sheet_obj.max_column
    last_column_name = get_col_name(last)
    if last_column_name != str(today):
        print("Adding new column, number of columns:", last)
        cell = sheet_obj.cell(row=1, column=last+1)
        cell.value = str(today)
        last += 1
        for i in range(2, sheet_obj.max_row+1):
            cell = sheet_obj.cell(row=i, column=last)
            cell.value = 'A'
        wb_obj.save(path)
    return last

def get_col_name(colnum):
    wb_obj = openpyxl.load_workbook(path) 
    sheet_obj = wb_obj.active 
    cell = sheet_obj.cell(row=1, column=colnum)
    return cell.value

def write_attendance_in_xl(name, data, count):
    roll_no = int(name.split('_')[0])
    stud_name = " ".join(name.split('_')[1:])
    lastColumn = add_column()
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj[datetime.now().strftime("%B")]
    for key, value in data.items():
        if stud_name in value and roll_no in value:
            cell = sheet_obj.cell(row=key, column=lastColumn)
            print(cell.value)
            if cell.value == "A":
                cell.value = 'In-time: ' + str(datetime.now().time()).split('.')[0]
                count+=1
            elif cell.value.startswith("In-time:"):
                in_time = cell.value.split(' ')[1]
                cell.value = 'In-time: ' + str(in_time) + ' \nOut-time: ' + str(datetime.now().time()).split('.')[0]
    wb_obj.save(path)
    return count

def fetch_attendance(data):
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj[datetime.now().strftime("%B")]
    roll_no = int(input("Enter your roll number: "))
    for key, value in data.items():
        if roll_no in value:
            attendance_records = PrettyTable(['Date', 'In-time', 'Out-time', 'Hours'])
            print("\nAttendance records for the month of ", datetime.now().strftime("%B"))
            print ("Name: ", value[1])
            for i in range(3, sheet_obj.max_column+1):
                cell = sheet_obj.cell(row=key, column=i)
                if cell.value.startswith("In-time:"):
                    in_time = cell.value.split(' ')[1]
                    out_time = cell.value.split(' ')[3]
                    hours = str((datetime.strptime(out_time, '%H:%M:%S') - datetime.strptime(in_time, '%H:%M:%S')).total_seconds()/3600)[:4]
                    attendance_records.add_row([get_col_name(i), in_time, out_time, hours])
                else:
                    attendance_records.add_row([get_col_name(i), 'A', 'A', 0])
            print (attendance_records)
            break
    else:
        print("\nNo record found for this roll number.")
    print("\n")
    input("Press any key to continue...")

def send_email(receiver, subject=None, data=None):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("d2021.piyush.chugeja@ves.ac.in", os.getenv('EMAIL_PASSWORD'))
    sender_email = "d2021.piyush.chugeja@ves.ac.in"
    message = MIMEMultipart("alternative")
    message["From"] = "Attendance system"
    message["To"] = receiver['email']
    message["Subject"] = subject if subject is not None else "Attendance report"
    if data is None:
        text = """\
        Hi {receiver[name]},
        Your attendance for this month is {receiver[attendance]}%.
        """.format(receiver=receiver)
        html = """\
        <html>
            <body>
                <h1 align='center'>Email from attendance system</h1>
                <hr>
                <p>
                    Hi {receiver[name]},<br>
                    Your attendance for this month is {receiver[attendance]}%.<br>
                </p>
                """ + """
            </body>
        </html>
        """.format(receiver=receiver)
    else:
        text = data
        html = """\
        <html>
            <body>
                <h1 align='center'>Email from attendance system</h1>
                <hr>
                <p>
                    {data}
                </p>
            </body>
        </html>
        """.format(data=data)
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    s.sendmail(sender_email, receiver['email'], message.as_string())
    s.quit()

def calculate_attendance(data):
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj[datetime.now().strftime("%B")]
    for key, value in data.items():
        if key!=1:
            total_classes = 0
            attended_classes = 0
            for i in range(3, sheet_obj.max_column+1):
                cell = sheet_obj.cell(row=key, column=i)
                if cell.value.startswith("In-time:"):
                    total_classes += 1
                    attended_classes += 1
                elif cell.value == "A":
                    total_classes += 1
            attendance = round((attended_classes/total_classes)*100, 2)
            receiver = {'email':value[4], 'name':value[1], 'attendance':attendance}
            send_email(receiver)

def send_monthly_attendance(month = datetime.now().strftime("%B")):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    sender_email = "d2021.piyush.chugeja@ves.ac.in"
    s.login(sender_email, os.getenv('EMAIL_PASSWORD'))
    workbook = openpyxl.load_workbook(path)
    attendance_all = workbook[month]
    member_rows = get_dict()
    attendance_html_table = '''
    <table border="1" style="border-collapse: collapse; width: 100%;">
        <tr>
            <th>Date</th>
            <th>In-time</th>
            <th>Out-time</th>
            <th>Hours</th>
        </tr>
    '''
    for key, value in member_rows.items():
        if key != 1:
            message = MIMEMultipart("alternative")
            message["From"] = "Attendance System"
            total, attended = 0, 0
            for i in range(3, attendance_all.max_column+1):
                cell = attendance_all.cell(row=key, column=i)
                total += 1
                date = attendance_all.cell(row=1, column=i).value
                if cell.value.startswith("In-time:"):
                    attended += 1
                    in_time = cell.value.split(' ')[1]
                    try:
                        out_time = cell.value.split(' ')[3]
                        hours = str((datetime.strptime(out_time, '%H:%M:%S') - datetime.strptime(in_time, '%H:%M:%S')).total_seconds()/3600)[:4]   
                    except:
                        out_time = "Unavailable"
                        hours = "-"
                    attendance_html_table += '''
                    <tr>
                        <td>{date}</td>
                        <td>{in_time}</td>
                        <td>{out_time}</td>
                        <td>{hours}</td>
                    </tr>
                    '''.format(date=date, in_time=in_time, out_time=out_time, hours=hours)
                else:
                    attendance_html_table += '''
                    <tr>
                        <td>{date}</td>
                        <td>A</td>
                        <td>A</td>
                        <td style = 'background: red;'>0</td>
                    </tr>
                    '''.format(date=date)
            attendance = round((attended/total)*100, 2)
            attendance_html_table += '''
            </table>
            <br>
            <p>
                Overall attendance for {month} is {attendance}%.
            '''.format(month=month, attendance=attendance)
            receiver = {'email':value[2], 'name':value[1]}
            
            text = """\
            Hi {receiver[name]},
            Your attendance for this month is {attendance}%.
            """.format(receiver=receiver, attendance=attendance)
            
            html = """\
            <html>
                <body>
                    <h1 align='center'>Email from attendance system</h1>
                    <hr>
                    <p>
                        Hi {receiver[name]},<br>
                        Here is your attendance record for the month of {month}:
                    </p>
                    <br>
                    {attendance_table}
                </body>
            </html>
            """.format(receiver=receiver, attendance=attendance, month=month, attendance_table=attendance_html_table)
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            message.attach(part1)
            message.attach(part2)
            message["To"] = receiver['email']
            message["Subject"] = "Attendance report for {month}".format(month=month)
            print("Sending email to {receiver[name]} {receiver[email]}...".format(receiver=receiver))
            s.send_message(message)
    s.quit()