def area_triangulo():
    """Calcula el área de un triángulo a partir de la base y la altura ingresadas por el usuario."""
    base = float(input("Escriba la base del triangulo: "))
    altura = float(input("Escriba la altura del triangulo: "))
    area = (base*altura)/2
    print(f"El área del triangulo con base {base} y altura {altura} es: {area:.2f}")

def main():
    area_triangulo()


if __name__ == "__main__":
    main()