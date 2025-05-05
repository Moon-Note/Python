import numpy as np

a = np.array([[1, 2, 3], [4, 5,6]])

print('axis0 : ', np.amin(a, axis=0))
print('axis1 : ', np.amin(a, axis=1))