import openpyxl 
from datetime import datetime
from prettytable import PrettyTable
path = "Attendance.xlsx"

def get_dict():
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active 
    max_r = sheet_obj.max_row
    cell_obj = sheet_obj['A1': 'B'+str(max_r)]
    dict = {}
    for cell1, cell2 in cell_obj:
        dict[cell1.row] = [cell2.value, cell1.value]
    return dict

def add_column():
    today = datetime.date(datetime.now())
    wb_obj = openpyxl.load_workbook(path) 
    sheet_obj = wb_obj.active 
    last = sheet_obj.max_column
    last_column_name = get_col_name(last)
    if last_column_name != str(today):
        cell = sheet_obj.cell(row=1, column=last+1)
        cell.value = str(today)
        # initialise all values in the new column as Absent
        for i in range(2, sheet_obj.max_row+1):
            cell = sheet_obj.cell(row=i, column=last+1)
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
    sheet_obj = wb_obj['Sheet1']
    for key, value in data.items():
        if stud_name in value and roll_no in value:
            cell = sheet_obj.cell(row=key, column=lastColumn)
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
    sheet_obj = wb_obj.active
    roll_no = int(input("Enter your roll number: "))
    for key, value in data.items():
        if roll_no in value:
            attendance_records = PrettyTable(['Date', 'In-time', 'Out-time', 'Hours'])
            print ("\nName: ", value[1])
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
    