import numpy as np
#3x + 2y = 12  b3x + 2y = 12  
#x - 4y = -5

A = np.array([[3,2],
              [1,-4]])

B = np.array([12,-5])

solu = np.linalg.solve(A,B)

print(solu)
print(solu.dtype)
