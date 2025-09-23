class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = True

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre
        
        self.libros = []

    

class Prestamo:
    def __init__(self,libro):
        self.libro = libro
        
    def disponible(self):
        if not self.libro.estado:
            return False
        return True
    
    def cambiar_estado(self):
        if not self.disponible():
            print("El libro no esta disponible")
            return False
        
        self.libro.estado = False
        return True

libro1 = Libro("los100","unknown")

us1 = Usuario("carlos")



            

    