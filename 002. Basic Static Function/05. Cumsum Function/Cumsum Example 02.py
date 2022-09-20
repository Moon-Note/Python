import numpy as np

a = [[1,2,3], [4,5,6]]

print('axis0 result:', np.cumsum(a, axis=0))
print('axis1 result:', np.cumsum(a, axis=1))