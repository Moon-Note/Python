from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

# 새 워크북 생성 및 활성화된 워크시트 선택
wb = Workbook()
ws = wb.active

# 데이터 추가
data = [
    ['Month', 'Value1', 'Value2'],
    ['Jan', 10, 40],
    ['Feb', 20, 30],
    ['Mar', 30, 20],
    ['Apr', 40, 10]
]

for row in data:
    ws.append(row)

# 차트에 사용할 데이터 범위 지정 (값 범위)
values = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=5)

# 차트 객체 생성
line_chart = LineChart()
line_chart.add_data(values, titles_from_data=True)

# 차트의 X축에 대한 범주 범위 지정 (레이블 범위)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)
line_chart.set_categories(categories)

# 차트 제목 설정
line_chart.title = "Sample Line Chart"

# 차트를 워크시트에 추가 (차트가 나타날 위치 지정)
ws.add_chart(line_chart, "E5")

# 워크북 저장
wb.save("line_chart_example.xlsx")
