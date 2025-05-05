import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])

print('1D Array')
print(np.percentile(a, 25))
print(np.percentile(a, 50))
print(np.percentile(a, 75))

print('2D Array - Case: axis=0')
print(np.percentile(b, 25, axis=0))
print(np.percentile(b, 50, axis=0))
print(np.percentile(b, 75, axis=0))

print('2D Array - Case: axis=1')
print(np.percentile(b, 25, axis=1))
print(np.percentile(b, 50, axis=1))
print(np.percentile(b, 75, axis=1))