import numpy as np

a=np.arange(0,12)

matriz=np.array([
    a[0:4],
    a[4:8],
    a[8:12]
])

#tranformando la matriz con reshape
matriz2=a.reshape(3,4)

print(matriz.shape)
print(matriz.ndim)

print(matriz2.shape)
print(matriz2.ndim)