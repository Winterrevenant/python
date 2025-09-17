class Libro:
    """Clase que representa un libro con disponibilidad para préstamo."""
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self._disponible = True

    def prestar(self) -> bool:
        
        if not self._disponible:
            print(f"El libro {self.titulo} no esta disponible")
            return False
        self._disponible=False
        print(f"El libro {self.titulo} esta disponible")
        return True


libro1 = Libro("Los 100","Kass Morgan")
libro1.prestar()
libro1.prestar()

