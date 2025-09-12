import numpy as np

a = np.array([[5, 10, 15],
              [20, 25, 30],
              [35, 40, 45]])

#Primeras dos filas
print(a[:2])
#Ultimas dos Columnas
print(a[:3,1:])
#Una submatriz de 2x2 que contenga los valores 25, 30, 40, 45
matriz=a[1:3,1:3]
print(matriz)