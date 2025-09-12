import numpy as np

manzana = np.array([1,0])

platano = np.array([2,1])

weights = np.array([[1.0],
                    [2.0]])

bias = np.array([-2.0])

def capa_densa(inputs,weights,bias):
    return np.dot(inputs,weights)+bias


def sigmoid(x):
    return 1/(1+np.exp(-x))

# Clasificar manzana
salida_manzana = sigmoid(capa_densa(manzana, weights, bias))
print("Probabilidad de que sea plátano (manzana):", salida_manzana)

# Clasificar plátano
salida_platano = sigmoid(capa_densa(platano, weights, bias))
print("Probabilidad de que sea plátano (plátano):", salida_platano)
