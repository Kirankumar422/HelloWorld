import xlrd

loc = "E:/office/worksheet2.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    print("The column name: {}".format(sheet.cell_value(0, i)))
