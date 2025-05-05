from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from pandas import DataFrame

# 새 워크북 생성
workbook = Workbook()

# 현재 활성화된 시트 선택
sheet = workbook.active

# 중복 데이터를 포함하는 DataFrame 생성
data = {'1st score': [100, 95, 100, 90, 100],
        '2nd score': [90, 100, 100, 95, 100],
        '3rd score': [100, 95, 100, 90, 100]}
df = DataFrame(data, index=None)

# 열 기준 중복제거한 값 확인
print(df.loc[:, ~df.T.duplicated()])

# DataFrame의 데이터를 시트에 작성
for row in dataframe_to_rows(df.loc[:, ~df.T.duplicated()], index=False, header=True):
    sheet.append(row)

# 워크북 저장
workbook.save('[Exam 02]Remove_duplicates_by_column.xlsx')
