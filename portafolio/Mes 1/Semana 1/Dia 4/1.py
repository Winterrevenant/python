#Lista de frutas para recorrer

def imprimir_frutas(frutas):
    """Imprime las frutas separadas por coma."""
    print(", ".join(frutas))




def main():
    frutas = ["Coco","Uva","Manzana","Pera","Liche"]
    imprimir_frutas(frutas)

if __name__=="__main__":
    main()


