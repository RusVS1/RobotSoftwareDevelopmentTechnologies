import sys
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

data = []

for line in sys.stdin:
    line = line.split()
    line = [line[0], int(line[1]), float(line[2])]
    data.append(line)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Товары"
sheet['A1'] = "Название"
sheet['B1'] = "Количество"
sheet['C1'] = "Цена"

str_c = 2
for line in data:
    sheet['A' + str(str_c)] = line[0]
    sheet['B' + str(str_c)] = line[1]
    sheet['C' + str(str_c)] = line[2]
    str_c += 1
    
wb.save('test.xlsx')