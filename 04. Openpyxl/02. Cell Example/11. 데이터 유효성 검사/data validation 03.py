from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation

# 워크북 및 시트 생성
wb = Workbook()
ws = wb.active

# 데이터 유효성 검사 규칙: 드롭다운 목록 생성
dropdown_list = DataValidation(
    type="list", 
    formula1='"Yes,No,Maybe"', 
    showDropDown=False
)
dropdown_list.prompt = "값을 선택하세요."
dropdown_list.promptTitle = "드롭다운 목록"

# 데이터 유효성 검사 규칙을 시트에 추가
ws.add_data_validation(dropdown_list)

# 특정 셀에 유효성 검사 규칙을 적용
dropdown_list.add(ws["B1"])

# 워크북 저장
wb.save("dropdown_example.xlsx")
