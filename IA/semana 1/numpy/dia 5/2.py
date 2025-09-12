import numpy as np

a = np.array([[1,2],
              [2,6]])


det = np.linalg.det(a)

print("La determinante es:",det)
if det != 0:
    inv_a = np.linalg.inv(a)

    print("Inversa de A:\n",inv_a)

    print("Verificacion")

    res = a@inv_a

    print(res)