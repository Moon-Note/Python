from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()

# Select the activated workbook
sheet = workbook.active

# Write the A1 value to 'Hello'
sheet['A1'] = 'Hello'
# The coordinate output of the A1 cell
cell = sheet['A1']
print(cell.coordinate)  # Output: A1

# Write the B2 value to 'World'
sheet['B2'] = 'World'
# The coordinate output of the B2 cell
cell = sheet.cell(row=2, column=2)
print(cell.coordinate)  # Output: B2

# Write the C3 value to 'World'
sheet['C3'] = 'Created by MoonNote'
# The coordinate output of the C3 cell
cell = sheet['C3']
print(cell.coordinate)  # Output: C3

# save the file
workbook.save('Openpyxl Coordinate Example.xlsx')