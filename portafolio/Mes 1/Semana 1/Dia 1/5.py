def comprobar_edad():
    """
    Pide al usuario que escriba su edad
    y usa condicionales if/elif/else para clasificarlo.
    """
    try:
        edad_usuario = int(input("Introduzca su Edad: "))
        # Clasificar según la edad ingresada

        if edad_usuario < 18:
            print("Eres menor de Edad")
        elif 18 <= edad_usuario <= 65:
            print("Eres adulto")
        else:
            print("Eres adulto mayor")
    except ValueError:
        print("Error: la edad debe ser un numero entero")
    
    

def main():
    comprobar_edad()


if __name__ == "__main__":
    main()
    