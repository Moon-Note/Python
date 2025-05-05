import numpy as np

a = np.array([1, 1, 2, 3, 3, 3, 4, 4, 5])

print(np.unique(a, return_index=True, return_inverse=True, return_counts=False))