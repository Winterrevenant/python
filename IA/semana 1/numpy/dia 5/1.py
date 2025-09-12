import numpy as np

A = np.array([[2, 3],
              [1, 4]])


deter = np.linalg.det(A)

inver = np.linalg.inv(A)

res = A @ inver

print(deter)

print(inver)

print(res)
