import numpy as np

a = [[1,2], [3,4], [5,6]]

print('1st result(F/T/F) : ')
print(np.extract([False,True,False],a))
print('2nd result(T/F/T) : ')
print(np.extract([True,False,True],a))
