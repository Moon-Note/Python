import numpy as np

a = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 5, 8, 8, 9]

print(np.unique(a, return_index=True)) 
print(np.unique(a, return_inverse=True))
print(np.unique(a, return_counts=True))