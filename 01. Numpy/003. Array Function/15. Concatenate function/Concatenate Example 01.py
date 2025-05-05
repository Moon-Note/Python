import numpy as np

# 두 배열을 행 기준으로 연결
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.concatenate((a, b), axis=0)
print(result)
# 출력:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
