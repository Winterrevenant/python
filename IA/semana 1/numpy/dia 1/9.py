import numpy as np

a=np.linspace(1,9,9)

matriz=a.reshape(3,3)

matriz=matriz*2

#matriz manuak
matriz2=np.array([
    a[0:3],
    a[3:6],
    a[6:9]
])

matriz2=matriz2*2



print(matriz.shape,matriz.dtype,matriz.ndim)
print(matriz2.shape,matriz2.dtype,matriz2.ndim)
