import numpy as np

x = np.arange(16.0).reshape(4, 4)
output = np.hsplit(x, 2)

print('x 배열 :\n', x)
print('1번째 split 배열 :\n', output[0])
print('2번째 split 배열 :\n', output[1])