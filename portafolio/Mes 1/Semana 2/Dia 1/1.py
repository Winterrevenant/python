class Libro:
    """Clase que representa un libro con disponibilidad para préstamo."""
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self._disponible = True
    
    def is_disponible(self):
        
        if not self._disponible:
            return False
        return True

    def cambiar_estado(self):
        if not self._disponible:
            return False
        self._disponible = False

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def prestar(self,libro):
        if Libro.is_disponible(libro):
            Libro.cambiar_estado(libro)
        else:
            print(f"El libro {libro.titulo} no esta disponible")

    
def main():

    libro1 = Libro("Los 100","Kass Morgan")

    usu1 = Usuario("W")

    usu2 = Usuario("X")

    usu1.prestar(libro1)
    usu2.prestar(libro1)
    
    
    
if __name__ == "__main__":
    
    main()
