from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation

# 워크북 및 시트 생성
wb = Workbook()
ws = wb.active

# 데이터 유효성 검사 규칙: 1에서 100 사이의 숫자만 입력 가능
dv = DataValidation(type="whole", operator="between", formula1=1, formula2=100, showErrorMessage=True)
dv.error = "입력 값이 잘못되었습니다. 1에서 100 사이의 숫자만 입력하세요."
dv.errorTitle = "잘못된 입력"

# 특정 셀에 규칙 적용
ws.add_data_validation(dv)
dv.add("A1")

# 파일 저장
wb.save("data_validation_example.xlsx")
