from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.formatting.rule import FormulaRule

# 새 워크북과 워크시트 생성
wb = Workbook()
ws = wb.active

# 예제 데이터 추가
data = [
    ["이름", "수익"],
    ["A", 1000],
    ["B", 1500],
    ["C", -500],
    ["D", 2000],
    ["E", -100]
]

for row in data:
    ws.append(row)

# 조건부 서식 규칙 설정: 수익이 음수인 경우 글꼴 색을 빨간색으로 변경
font = Font(color="FF0000")
rule = FormulaRule(formula=["B2<0"], font=font)
ws.conditional_formatting.add("B2:B6", rule)

# 워크북 저장
wb.save("conditional_formatting_formula_example.xlsx")
