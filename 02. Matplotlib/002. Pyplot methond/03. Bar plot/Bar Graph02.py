import matplotlib.pyplot as plt

# 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
colors = ['red', 'blue', 'green', 'purple', 'orange']

# 색상을 지정한 막대 그래프 생성
plt.bar(categories, values, color=colors)
plt.title("Bar Plot with Colors and Labels")
plt.xlabel("Categories")
plt.ylabel("Values")

# 각 막대 위에 값 표시
for i, value in enumerate(values):
    plt.text(i, value + 0.2, str(value), ha='center', fontsize=12)

plt.show()
