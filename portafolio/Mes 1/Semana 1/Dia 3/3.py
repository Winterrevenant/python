mensaje = "Global"

def funcion_local():
    """Demuestra la diferencia entre variable local y global."""
    mensaje = "Local"
    return mensaje


def main():
    print(f"Variable global: {mensaje}")
    print(f"Variable local: {funcion_local()}")


if __name__=="__main__":
    main()