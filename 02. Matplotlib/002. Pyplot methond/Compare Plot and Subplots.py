import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# 여러 서브플롯 생성
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Sine')

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('Cosine')

axs[1, 0].plot(x, np.tan(x))
axs[1, 0].set_title('Tangent')

axs[1, 1].plot(x, np.exp(x))
axs[1, 1].set_title('Exponential')

# 레이아웃 조정
plt.tight_layout()
plt.show()


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
