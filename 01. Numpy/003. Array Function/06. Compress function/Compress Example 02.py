import numpy as np

a = [[1,2], [3,4], [5,6]]

print('1st result(F/T/F) : ')
print(np.compress([False,True,False],a, axis=0))
print('2nd result(T/F/T) : ')
print(np.compress([True,False,True],a, axis=0))
