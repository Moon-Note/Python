import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)  # 색상을 위한 값
sizes = 1000 * np.random.rand(50)  # 크기를 위한 값

# 색상과 크기를 지정한 산점도 생성
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.title("Scatter Plot with Color and Size")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.colorbar()  # 색상 바 추가
plt.show()
