def num_par_impar():
    """Pide un numero al usuario y verifica si el numero es par o impar"""
    try:
        num = int(input("Escriba un Numero: "))
        
        if num%2 ==0:
            print("El numero es par")
        else:
            print("El numero es impar")
    except ValueError:
        print("Error: escriba un numero entero")



def main():
    num_par_impar()


if __name__=="__main__":
    main()