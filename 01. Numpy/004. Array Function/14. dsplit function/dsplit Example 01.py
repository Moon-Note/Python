import numpy as np

x = np.arange(16.0).reshape(2, 2, 4)
output = np.vsplit(x, 2)

print('x 배열 :\n', x)
print('dsplit 배열 :\n', output)