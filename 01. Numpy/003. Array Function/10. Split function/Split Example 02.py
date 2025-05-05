import numpy as np

x = np.arange(8.0)
output = np.split(x, [3, 5, 6, 10])

print(output)
