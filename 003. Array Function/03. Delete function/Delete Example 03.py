import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])

a = np.delete(a, np.s_[::2], 0)
print('delete data from Axis = 0 : ')
print(a)

a = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])

a = np.delete(a, np.s_[::2], 1)
print('delete data from Axis = 1 : ')
print(a)


