import openpyxl

file = "C:/Users/Alkesh/vsc_workspace/Python_Selenium/Write.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook.active

for r in range(1, 6):
    for c in range(1, 6):
        sheet.cell(r, c).value = "Nice"

workbook.save(file)
