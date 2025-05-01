import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print('axis=0 :\n',np.concatenate((a, b), axis=0))
print('axis=1 :\n',np.concatenate((a, b.T), axis=1))
print('axis=none :\n',np.concatenate((a, b), axis=None))