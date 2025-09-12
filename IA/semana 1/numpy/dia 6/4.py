import numpy as np

#x + y + z = 6  
#2x - y + z = 3  
#-x + 2y - z = 2

A = np.array([[1,1,1],
              [2,-1,+1],
              [-1,2,-1]])

B = np.array([6,3,2])

solu = np.linalg.solve(A,B)

print(solu)