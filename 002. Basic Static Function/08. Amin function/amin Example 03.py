import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print('axis0 : ', np.amin(a, axis=0, where=[False, True, False], initial=9))
print('axis1 : ', np.amin(a, axis=1, where=[False, False, True], initial=9))