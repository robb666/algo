import numpy as np
from math import sqrt


arr = [5, 4, 2, 3]

std_dev = sqrt(sum([(i - (sum(arr) / len(arr))) ** 2 for i in arr]) / len(arr))
print(std_dev)


avg = np.divide(np.sum(arr), np.array(arr).shape[0])
np_std_dev = np.sqrt(np.divide(np.sum([np.power(i - avg, 2) for i in np.nditer(arr)]), np.array(arr).shape[0]))
print(np_std_dev)