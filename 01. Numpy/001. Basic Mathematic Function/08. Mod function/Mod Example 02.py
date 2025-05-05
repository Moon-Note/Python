import numpy as np

x1 = np.arange(9.0).reshape((3,3))
x2 = np.arange(3.0)

#함수 이용
a = np.mod(x2, x1)
#연산자 이용
b = x2 % x1

#결과 같음
print(a)
print(b)