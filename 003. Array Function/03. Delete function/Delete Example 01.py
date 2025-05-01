import numpy as np

a = np.arange(1, 10, 1)
print('Initial np values : ', a)

a = np.delete(a, 0)
print('1st delete data : ', a)
a = np.delete(a, 1)
print('2nd delete data : ', a)
a = np.delete(a, 2)
print('3rd delete data : ', a)
a = np.delete(a, 3)
print('4th delete data : ', a)
a = np.delete(a, 4)
print('5th delete data : ', a)