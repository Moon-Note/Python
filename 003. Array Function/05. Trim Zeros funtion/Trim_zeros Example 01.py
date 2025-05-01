import numpy as np

a = [0, 0, 0, 1, 2, 3, 4, 0, 0, 0]

print(np.trim_zeros(a, 'f'))
print(np.trim_zeros(a, 'b'))
print(np.trim_zeros(a))