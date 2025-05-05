import numpy as np


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
output = np.dsplit(arr, [1, 2])

# Displaying the resulting 2D arrays
for idx, array in enumerate(output):
    print(f"2D Array {idx + 1}:")
    print(array)
    print()
