import openpyxl

from openpyxl import Workbook

# You must change the physical path before running this script.
currPath = "C:/Users/natio/OneDrive - 성균관대학교/99. Personal Blog/05. Python/05. OPENPYXL_XLRD_XLWT/01. Excel Sheet/"

# Load the excel file
wb = openpyxl.load_workbook(filename=currPath+"Sample Sheet File.xlsx")

active_sheetname = "Sample Sheet"
ws = wb[active_sheetname]

ws.sheet_properties.tabColor = "FF0000"

wb.save(filename=currPath+"Sample Sheet File2.xlsx")
