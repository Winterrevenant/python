class Libro:
    """Clase que representa un libro con disponibilidad para préstamo."""
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self._disponible = True
    
    def is_disponible(self) -> bool:
        return self._disponible

    def prestar(self) -> bool:
        """Intenta marcar el libro como no disponible. True si se prestó, False si ya estaba prestado."""
        if not self._disponible:
            return False
        self._disponible = False
        return True
    
    def devolver(self) -> bool:
        """Intenta marcar el libro como disponible. True si se devolvió, False si ya estaba disponible."""
        if self._disponible:
            return False
        self._disponible = True
        return True
    
class Usuario:
    """Clase que representa un usuario que puede tomar prestado un libro"""
    def __init__(self,nombre:str):
        self.nombre = nombre

    def prestar(self,libro:Libro) -> None:
        if libro.prestar():
            print(f"{self.nombre} ha prestado {libro.titulo}.")
        else:
            print(f"{libro.titulo} no esta disponible")
    
    
def main():

    libro1 = Libro("Los 100","Kass Morgan")

    usu1 = Usuario("W")

    usu2 = Usuario("X")

    usu1.prestar(libro1)
    usu2.prestar(libro1)
    
    
    
    
if __name__ == "__main__":
    
    main()
