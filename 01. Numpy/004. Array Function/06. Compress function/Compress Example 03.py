import numpy as np

a = [[1,2], [3,4], [5,6]]

print('1st result(F/T/F) : ')
print(np.compress([0,1,0],a, axis=0))
print('2nd result(T/F/T) : ')
print(np.compress([1,0,1],a, axis=0))
