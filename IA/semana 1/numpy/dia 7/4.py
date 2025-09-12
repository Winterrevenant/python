import numpy as np

# Entradas: [tamaño, color]
X = np.array([
    [1, 0],  # manzana
    [2, 1],  # plátano
    [1, 1],  # plátano pequeño
    [2, 0],  # manzana grande
])

# Etiquetas: 0 = manzana, 1 = plátano
y = np.array([0, 1, 1, 0])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Inicializamos pesos y bias aleatoriamente
np.random.seed(1)
weights = np.random.rand(2)
bias = np.random.rand()

# Entrenamos por 1000 iteraciones
for epoch in range(1000):
    # Paso hacia adelante
    z = np.dot(X, weights) + bias
    output = sigmoid(z)

    # Calculamos el error
    error = y - output

    # Ajustamos pesos y bias
    adjustments = error * sigmoid_derivative(output)
    weights += np.dot(X.T, adjustments) * 0.1
    bias += np.sum(adjustments) * 0.1

def predecir(fruta):
    resultado = sigmoid(np.dot(fruta, weights) + bias)
    return "Plátano 🍌" if resultado > 0.5 else "Manzana 🍎"

print(predecir([1, 0]))  # manzana
print(predecir([2, 1]))  # plátano
print(predecir([1, 1]))  # plátano pequeño
print(predecir([2, 0]))  # manzana grande
