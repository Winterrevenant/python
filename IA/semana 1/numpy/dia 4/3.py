import numpy as np

C = np.array([[1, 2, 3],
              [4, 5, 6]])
D = np.array([[7, 8],
              [9, 10],
              [11, 12]])

res = C @ D

print(res)
print(res.shape)