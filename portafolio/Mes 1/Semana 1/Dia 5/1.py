def menu():
    """Funcion que sirve para crear el menu"""
    print("---Gestor de Tareas---")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")


def añadir_tarea(lista):
    """Funcion que pide al usuario una tarea y categoria para agregar a la agenda"""
    dicc={}
    try:
        tarea = str(input("Ingrese el nombre de la tarea: "))
        categoria = str(input("Ingrese la categoría: "))
        dicc ['tarea'] = tarea
        dicc ["categoria"]=categoria
        return dicc
        
    except ValueError:
        print("Error. Ingrese una tarea valida")


def listar_tareas(lista):
    """Funcion que lista las tareas pendientes si hay en una tabla"""
    if not lista:
        print("No hay tareas pendientes")
        return None
    print(f"{"Tarea":<10} | {"Categoria":>10}")
    print("-"*23)
    for i in lista:
        print(f"{i['tarea']:<10} | {i['categoria']:>10}")

def eliminar_tarea(lista):
    if not lista:
        print("No hay tareas para eliminar")
        return None
    print(f"{"ID":<10} | {"Tarea":^10} | {"Categoria":>10}")
    print("-"*37)
    contador = 1
    for i in lista:
        print(f"{contador:<10} | {i['tarea']:^10} | {i['categoria']:>10}")
        contador+=1
    eliminar = int(input("Escribe el ID de la tarea para eliminar"))
    

def main():
    lista_tareas=[{"tarea":"comprar pan","categoria":"hogar"}]
    menu()
    eliminar_tarea(lista_tareas)
    

if __name__=="__main__":
    main()