from openpyxl import load_workbook

wb = load_workbook("large_file.xlsx", read_only=True)
ws = wb.active

for row in ws.iter_rows(min_row=1, max_col=3, max_row=10):
   print([cell.value for cell in row])

