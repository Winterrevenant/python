import numpy as np

# 3 entradas (pueden representar características como temperatura, presión, etc.)

inputs = np.array([1.0,2.0,3.0])

# Matriz de pesos: 3 entradas → 2 salidas

weights = np.array([[0.2,0.8],
                    [0.5,-0.91],
                    [-0.26,-0.27]])

output = np.dot(inputs,weights)

print("Salida sin activacion",output)

def relu(x):
    return np.maximum(0,x)
actived_output = relu(output)
print("Salida con Relu",actived_output)