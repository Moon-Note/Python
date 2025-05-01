import numpy as np

a = [[1,2], [3,4], [5,6]]

print('1st result(F/T/F) : ')
print(np.extract([0,1,0],a))
print('2nd result(T/F/T) : ')
print(np.extract([1,0,1],a))
