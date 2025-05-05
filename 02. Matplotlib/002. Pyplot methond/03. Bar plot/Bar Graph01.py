import matplotlib.pyplot as plt

# 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# 기본 막대 그래프 생성
plt.bar(categories, values)
plt.title("Basic Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
