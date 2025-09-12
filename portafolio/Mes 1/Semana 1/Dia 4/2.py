def calcular_promedio(diccionario):
    """Calcula el promedio de las notas del diccionario de un estudiante."""  

    promedio=sum(diccionario["notas"])/len(diccionario["notas"])
    return promedio


def main():
    dic_Estudiante = {
        "nombre":"Pedro",
        "edad":21,
        "notas":[8,7,10]
    }

    promedio=calcular_promedio(dic_Estudiante)
    print(f"El promedio de {dic_Estudiante['nombre']} es :{promedio:.2f}")

if __name__=="__main__":
    main()