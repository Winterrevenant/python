def menu():
    """Muestra el menu de opciones"""
    print("1:Consultar saldo")
    print("2:Depositar")
    print("3:Retirar")
    print("4:salir")
    


def consultar_saldo(Saldo):
    """Muestra el saldo actual"""
    print(f"Su saldo actual es ${Saldo:.2f}")

def depositar(Saldo):
    """Agrega el saldo si el monto es valido"""
    try:
        dinero = float(input("Escriba el monto a depositar: "))
        if dinero>0:
            Saldo+=dinero
            print(f"Deposito existoso.Nuevo saldo ${Saldo:.2f}")
        else:
            print("El monto debe ser mayor a cero")
    except ValueError:
        print("Error: debe ingresar un numero")
    return Saldo

def retirar(Saldo):
    """Agrega el saldo si el monto es valido"""
    try:
        dinero = float(input("Escriba el monto a retirar: "))
        if dinero<=0:
            print("Esl monto debe ser mayor a cero")
        elif dinero>Saldo:
            print("Fondos insuficientes")
        else:
            Saldo-=dinero
            print(f"Retiro existoso.Nuevo Saldo: ${Saldo:.2f}")
    except ValueError:
        print("Error: debe ingresar un numero")
    return Saldo

"""Funcion Principal donde se usan las funciones anteriores para simular un cajero"""
def main():
    Saldo = 1000
    while True:
        menu()
        try: 
            opcion = int(input("Elija una opcion: "))
            if opcion == 1:
                consultar_saldo(Saldo)
            elif opcion == 2:
               Saldo=depositar(Saldo)
            elif opcion == 3:
                Saldo=retirar(Saldo)
            elif opcion ==4:
                break
            else:
                print("Opcion no valida")
        except ValueError:
            print("Error:elijar una opcion valida")
    

if __name__ == "__main__":
    main()