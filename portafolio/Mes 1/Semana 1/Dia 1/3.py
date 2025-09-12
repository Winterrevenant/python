def datos_personales():
    #Pedir al usuario su nombre y edad
    nombre_usuario = input("Escriba su Nombre completo: ")
    try:
        edad_usuario = int(input("Escriba su Edad: "))
    except ValueError:
        print("Error: la Edad debe ser un Numero Entero")
        return
    # Mostrar resultados con formato
    print(f"Hola {nombre_usuario}, tienes {edad_usuario} años.")
    print(f"En 5 años tendrás {edad_usuario + 5}.")


def main():
    datos_personales()


if __name__ == "__main__":
    main()