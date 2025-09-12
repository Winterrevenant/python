import numpy as np

v1 = np.arange(1,4)
v2 = np.arange(4,7)

matriz = np.arange(1,7).reshape(2,3)

suma = v1+v2

res = v1-v2

multi = v1*v2

trans = matriz.T

print("Suma")
print(suma)
print("Resta")
print(res)
print("Multiplicacion")
print(multi)

print("Matriz Original")
print(matriz)
print("Transposicion")
print(trans)