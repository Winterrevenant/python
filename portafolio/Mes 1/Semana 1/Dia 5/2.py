def mostrar_menu():
    print("\n--- Gestor de Tareas (con IDs) ---")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea por ID")
    print("4. Salir")


def listar_tareas(tareas):
    """Muestra las tareas en formato tabla con ID."""
    if not tareas:
        print(" No hay tareas registradas.")
        return
    print(f"{'ID':>3} | {'Tarea':<25} | {'Categoría':<15} | {'Estado':<10}")
    print("-" * 62)
    for t in tareas:
        print(f"{t['id']:>3} | {t['nombre']:<25} | {t['categoria']:<15} | {t['estado']:<10}")


def anadir_tarea(tareas, next_id):
    """Añade una tarea con ID incremental único."""
    nombre = input("Nombre de la tarea: ").strip()
    categoria = input("Categoría: ").strip()

    # Verificar duplicados por nombre (opcional)
    for t in tareas:
        if t["nombre"].casefold() == nombre.casefold():
            print(" Esa tarea ya existe (evitamos duplicados).")
            return next_id

    tareas.append({
        "id": next_id,
        "nombre": nombre,
        "categoria": categoria,
        "estado": "pendiente",
    })
    print(f" Tarea añadida con ID {next_id}.")
    return next_id + 1


def eliminar_por_id(tareas):
    """Elimina una tarea según su ID único."""
    try:
        id_obj = int(input("Ingrese el ID de la tarea a eliminar: "))
    except ValueError:
        print(" Debe ingresar un número entero.")
        return

    for i, t in enumerate(tareas):
        if t["id"] == id_obj:
            tareas.pop(i)
            print(" Tarea eliminada.")
            return

    print(" No existe una tarea con ese ID.")


def main():
    tareas = []
    next_id = 1  # contador incremental para IDs

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            next_id = anadir_tarea(tareas, next_id)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            if not tareas:
                print(" No hay tareas para eliminar.")
            else:
                listar_tareas(tareas)
                eliminar_por_id(tareas)
        elif opcion == "4":
            print(" Saliendo del gestor...")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
