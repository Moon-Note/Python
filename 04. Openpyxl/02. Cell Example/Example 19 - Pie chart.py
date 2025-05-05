from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference

# 새 워크북 생성 및 활성화된 워크시트 선택
wb = Workbook()
ws = wb.active

# 데이터 추가
data = [
    ['Category', 'Value'],
    ['A', 30],
    ['B', 40],
    ['C', 20],
    ['D', 10]
]

for row in data:
    ws.append(row)

# 차트에 사용할 데이터 범위 지정 (값 범위)
values = Reference(ws, min_col=2, min_row=2, max_row=5)

# 차트 객체 생성
pie_chart = PieChart()
pie_chart.add_data(values, titles_from_data=False)

# 차트의 X축에 대한 범주 범위 지정 (레이블 범위)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)
pie_chart.set_categories(categories)

# 차트 제목 설정
pie_chart.title = "Sample Pie Chart"

# 차트를 워크시트에 추가 (차트가 나타날 위치 지정)
ws.add_chart(pie_chart, "E5")

# 워크북 저장
wb.save("pie_chart_example.xlsx")
