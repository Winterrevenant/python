import numpy as np

a = np.array([[5, 10, 15],
              [20, 25, 30],
              [35, 40, 45]])

#Extrae todas las filas en posiciones pares
print(a[::2])
#Extrae todas las columnas en posiciones impares
print(a[:,1::2])
#Extrae los valores en las esquinas del array
print(a[0,0],a[0,2],a[2,0],a[2,2])