class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = True

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.libros = []
    def prestar(self,libro):
        verificar = Prestamo(libro)
        if not verificar.disponible():
            print("Libro no disponible")
            return False
        if len(self.libros) > 3:
            print(f"Limite de libros alcanzado {len(self.libros)} de 3")


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
libro2 = Libro("perfume","unknown")
libro3 = Libro("hay un dinosaurio en mi sopa","unknown")
libro4 = Libro("harry poter","unknown")



us1 = Usuario("carlos")
us1.prestar(libro1)
us1.prestar(libro2)
us1.prestar(libro3)
us1.prestar(libro4)









            

    