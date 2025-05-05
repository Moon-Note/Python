import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print('axis0 : ', np.amax(a, axis=0, where=[False, True, False], initial=0))
print('axis1 : ', np.amax(a, axis=1, where=[True, True, True], initial=0))