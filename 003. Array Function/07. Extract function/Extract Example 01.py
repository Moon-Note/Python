import numpy as np

a = [1,2,3,4,5]
condition = [True, False, True, False, True]

print('Result : ', np.extract(condition, a))
