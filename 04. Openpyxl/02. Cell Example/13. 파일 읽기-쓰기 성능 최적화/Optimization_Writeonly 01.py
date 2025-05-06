# This code creates a new Excel file named "large_output.xlsx" and writes 10,000 rows of data to it.
# The write_only=True option allows for faster writing of large amounts of data by not keeping the workbook in memory.
# The write_only mode is particularly useful for large datasets where you don't need to read the data back into memory.
from openpyxl import Workbook
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "large_output.xlsx")

wb = Workbook(write_only=True)
ws = wb.create_sheet()

for i in range(1, 10001):
    ws.append([i, i * 2, i * 3])

wb.save(file_path)
wb.close()

print(f"파일이 저장되었습니다: {file_path}")
