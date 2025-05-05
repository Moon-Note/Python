import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# 산점도 생성
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='plasma')
plt.title("Advanced Scatter Plot with Annotations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.colorbar()

# 특정 데이터 포인트에 주석 추가
for i in range(len(x)):
    if sizes[i] > 700:  # 특정 크기 이상인 점들만 주석 추가
        plt.annotate(f'({x[i]:.2f}, {y[i]:.2f})', (x[i], y[i]), textcoords="offset points", xytext=(5,5), ha='center')

# 축 범위 설정
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.show()
