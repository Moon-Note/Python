import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values1 = [5, 7, 3, 8, 6]
values2 = [6, 8, 4, 7, 5]

x = np.arange(len(categories))  # 카테고리의 위치
width = 0.35  # 막대의 너비

# 그룹화된 막대 그래프 생성
plt.bar(x - width/2, values1, width, label='Dataset 1', color='lightblue')
plt.bar(x + width/2, values2, width, label='Dataset 2', color='lightgreen')

plt.title("Grouped Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.xticks(x, categories)  # X축 눈금 설정
plt.legend()

# 그래프 보정
plt.tight_layout()
plt.show()
