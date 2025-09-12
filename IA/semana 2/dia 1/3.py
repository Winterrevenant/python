import pandas as pd

series = pd.Series([5,8,7,7,8],
                   index=["Lunes","Martes","Miercoles","Jueves","Viernes"])

x = series["Miercoles"]
series["Viernes"] = 9

print(x)

dias_altos = series[series>7]

print(dias_altos)

