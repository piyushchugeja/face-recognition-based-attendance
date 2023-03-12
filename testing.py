import openpyxl
wb = openpyxl.load_workbook('Attendance.xlsx')
for sheet in wb.sheetnames:
    print(sheet)