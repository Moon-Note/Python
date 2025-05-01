import numpy as np

x = np.arange(8.0)
output = np.split(x, [3, 5, 6, 10])

print('1번째 Sub배열:' , output[0])
print('2번째 Sub배열:' , output[1])