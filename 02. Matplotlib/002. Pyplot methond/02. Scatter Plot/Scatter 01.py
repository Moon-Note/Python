import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
np.random.seed(0)  # 랜덤 시드 설정으로 동일한 결과 재현
x = np.random.rand(50)
y = np.random.rand(50)

# 기본 산점도 생성
plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
