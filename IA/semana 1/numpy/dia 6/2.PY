import numpy as np

A = np.array([[3,2],
              [1,-4]])

B = np.array([12,-5])

soluc = np.linalg.solve(A,B)

print("El resultado de [X,Y]:",soluc)