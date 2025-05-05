import numpy as np

a = np.ma.arange(3)
a[1] = np.ma.masked
b = np.arange(2, 5)
print('a :\n', a)
print('b :\n', b)

print('concatenate([a, b]) :\n', np.concatenate([a, b]))
print('ma.concatenate([a, b]) :\n', np.ma.concatenate([a, b]))