import numpy as np
#creacion de un array de manera manual
a = np.array([1,2,3,4])

print(f"Array:{a}")

#creacion de un array solo de ceros

ceros=np.zeros((2,3))
#creacion de un array solo de unos
unos=np.ones((3,2))

print("Ceros:\n",ceros)
print("Unos:\n", unos)

#rango de valores 

rango= np.arange(0,10,2)
print(f"Rango:{rango}")

#Espaciado Uniforme
linea=np.linspace(0,1,5)
print(f"Lineal: {linea}")

x = np.array([[1,2,3],[4,5,6]])
#poder visualizar cuantas filas y columnas tiene el array
print("Shape",x.shape)

print("Tipo de dato:", x.dtype)

print("Dimensiones:", x.ndim)