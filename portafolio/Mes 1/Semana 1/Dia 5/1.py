def normalizar(texto: str) -> str:
    """Reduce texto para comparaciones: sin espacios extremos y sin distinción de mayúsculas."""
    return texto.strip().casefold()
def menu():
    """Funcion que sirve para crear el menu"""
    print("---Gestor de Tareas---")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")


def añadir_tarea(lista,nombres_norm_set):
    """Añade una tarea si no existe ya (según nombre normalizado)."""
    nombre = input("Nombre de la tarea: ")
    categoria = input("Categoría: ")
    
    nombres_vis=nombre.strip()
    categoria_vis=categoria
    nombre_norm=normalizar(nombre)
    

    if nombre in nombres_norm_set:
        print("Esa tarea ya existe")
        return
    lista.append({
        "nombre":nombres_vis,
        "categoria":categoria_vis,
        "nombre_norm": nombre_norm,
    })
    nombres_norm_set.add(nombre_norm)


def listar_tareas(lista):
    """Funcion que lista las tareas pendientes si hay en una tabla"""
    if not lista:
        print("No hay tareas pendientes")
        return 
    print(f"{"Tarea":<10} | {"Categoria":>10}")
    print("-"*23)
    for t in lista:
        print(f"{t['nombre']:<10} | {t['categoria']:>10}")


def eliminar_tarea(lista):
    print(f"{"Tarea":<10} | {"Categoria":>10}")
    print("-"*23)

    for i in lista:
        print(f"{i['tarea']:<10} | {i['categoria']:>10}")
        
    eliminar = input("Escribe el nombre  de la tarea para eliminar: ")
    for i,j in enumerate(lista):
        if j["tarea"]==eliminar:
            lista.pop(i)
            return lista

def main():
    lista_tareas=[]
    nombres_norm_set=set()
    while True:
        try:
            menu()
            opcion = int(input("Elija una opcion: "))
            
            if opcion == 1:
                añadir_tarea(lista_tareas,nombres_norm_set)
            elif opcion == 2:
                listar_tareas(lista_tareas)
            elif opcion == 3:
                if not lista_tareas:
                    print("No hay tareas pendientes")
                else:
                    lista_tareas=eliminar_tarea(lista_tareas)
            elif opcion == 4:
                break
            else:
                print("Elija una opcion valida")
        except ValueError:
            print("Error: Escriba un numero entero valido")
  

if __name__=="__main__":
    main()