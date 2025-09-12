import pandas as pd

datos = {
    "Nombre":["Ana","Carlos","Oscar"],
    "Edad":[20,21,22],
    "Calificacion":[10,9,8]
}

df = pd.DataFrame(datos)

print(df)