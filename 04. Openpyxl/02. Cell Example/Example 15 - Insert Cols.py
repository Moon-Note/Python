from openpyxl import Workbook

# 새 워크북 생성
wb = Workbook()
ws = wb.active

# 초기 데이터 입력
ws.append(["Header1", "Header2", "Header3"])
ws.append(["Row1 Data1", "Row1 Data2", "Row1 Data3"])
ws.append(["Row2 Data1", "Row2 Data2", "Row2 Data3"])

# 두 번째 열에 빈 열 삽입
ws.insert_cols(2)

# 파일 저장
wb.save("inserted_cols.xlsx")
