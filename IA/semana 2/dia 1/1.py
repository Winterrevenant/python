import pandas as pd

serie = pd.Series([10,20,30,40], index=["a","b","c","d"])


datos = {
    "Nombre":["Ana","Luis","Carlos"],
    "Edad":[23,34,45],
    "Ciudad":["CDMX","MONTERREY","Guadalajara"]
}

df = pd.DataFrame(datos)

print(df)
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())