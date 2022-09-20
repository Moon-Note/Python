import numpy as np

x1 = np.arange(9.0).reshape((3,3))
x2 = np.arange(3.0)

#함수 이용
a = np.multiply(x1, x2)
#연산자 이용
b = x1 * x2

#결과 같음
print(a)
print(b)