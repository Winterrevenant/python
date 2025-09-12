class Libro:
    def __init__(self,titulo,autor,año):
        self.titulo=titulo
        self.autor=autor
        self.año=año
    def descripcion(self):
        print(f"Nombre:{self.titulo} Autor:{self.autor} Año:{self.año}")

libro1=Libro("Los 100","Unknown","2000")

libro1.descripcion()
