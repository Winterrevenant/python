import math
def area_circulo(radio):
    """Calcula el area de un circulo con el radio"""
    return math.pi*(radio**2)

def main():
    for i in [1,2,3]:
        print(f"Radio: {i}, Area: {area_circulo(i):.2f}")


if __name__=="__main__":
    main()