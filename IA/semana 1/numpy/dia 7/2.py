import numpy as np

inputs = np.array([1,2])

weigths = np.array([[0.5,-1],
                    [1.5,2]])

bias = np.array([0.1,-0.2])

output = np.dot(inputs,weigths) + bias

print(output)