import numpy as np

A = np.array([2, 4, 6])

C = np.array([[1, 2, 3],
              [4, 5, 6]])
D = np.array([[7, 8],
              [9, 10],
              [11, 12]])

res = A @ C
print(res)