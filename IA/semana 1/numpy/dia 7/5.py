import numpy as np

# Datos de entrada: [tamaño, color]
X = np.array([
    [1, 0],  # manzana
    [2, 1],  # plátano
    [1, 1],  # plátano pequeño
    [2, 0],  # manzana grande
])

# Etiquetas: 0 = manzana, 1 = plátano
y = np.array([0, 1, 1, 0])

# Función sigmoid y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Inicializamos pesos y bias
np.random.seed(1)
weights = np.random.rand(2)
bias = np.random.rand()

# Entrenamiento con seguimiento
for epoch in range(1, 21):  # Solo 20 iteraciones para ver el proceso
    # Paso hacia adelante
    z = np.dot(X, weights) + bias
    output = sigmoid(z)

    # Error
    error = y - output

    # Ajustes
    adjustments = error * sigmoid_derivative(output)
    weights += np.dot(X.T, adjustments) * 0.1
    bias += np.sum(adjustments) * 0.1

    # Mostrar progreso
    print(f"Iteración {epoch}")
    print(f"  Salida: {output.round(3)}")
    print(f"  Error: {error.round(3)}")
    print(f"  Pesos: {weights.round(3)}")
    print(f"  Bias: {round(bias, 3)}\n")
