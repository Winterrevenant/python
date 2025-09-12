def pedir_datos_persona():
    nombre = input("Escriba su Nombre: ")
    try:
        edad = int(input("Introduce tu Edad: "))
    except ValueError:
        print("La edad debe ser un numero entero. ")
        return
    print(f"Nombre: {nombre}, Edad: {edad}")




def main():
    pedir_datos_persona()

if __name__ =="__main__":
    main()