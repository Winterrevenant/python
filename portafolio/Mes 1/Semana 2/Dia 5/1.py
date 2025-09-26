class Libro:
    """Clase que sirve para simular un libro"""
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = True

class Usuario:
    """Clase que representa un usuario que puede tomar y devolver libros"""
    def __init__(self,nombre):
        self.nombre = nombre
        self.libros = []

    """Metodo que permite a un usuario tomar prestado un libro y lo agrega a su lista de libro prestados"""
    def prestar(self,libro) ->bool:
        verificar = Prestamo(libro)

        if not verificar.disponible():
            print("Libro no disponible")
            return False
        
        if len(self.libros) >= 3:
            print(f"Limite de libros alcanzado {len(self.libros)} de 3")
            return False

        print(f"Libro {libro.titulo} ha sido tomado prestado con exito por {self.nombre}")
        verificar.cambiar_estado()
        self.libros.append(libro)

    """Metodo que permite devolver el libro prestado"""
    def devolver(self,libro):
        verificar = Prestamo(libro)

        if not verificar.disponible():
            verificar.cambiar_estado()
            print(f"Libro {libro.titulo} ha sido de vuelto con exito por {self.nombre}")

class Prestamo:
    """Clase que sirve para controlar los prestamos del libro"""
    def __init__(self,libro):
        self.libro = libro

    """Metodo que verifica si el libro esta disponible """    
    def disponible(self) ->bool:
        if not self.libro.estado:
            return False
        return True
    
    """Metodo que cambiaba el estado de un libro dependendiendo si esta o no esta disponible"""
    def cambiar_estado(self) ->bool:
        if not self.disponible():
            self.libro.estado = True
            return False  
        self.libro.estado = False
        return True

def caso1(libros,usu):
    """Caso 1 que pasa si el usuario quiere tomar prestado mas de 3 libros"""
    for i in libros:
        usu.prestar(i)

def caso2(libros,usu):
    """Caso 2 que pasa si el libro no esta disponible"""
    usu.prestar(libros[0])

def caso3(libros,usu1,usu2):
    """Devolver un libro para que este disponible"""    
    usu1.devolver(libros[0])
    usu2.prestar(libros[0])

def main():
    libros=[
    Libro("los100","unknown"),
    Libro("perfume","unknown"),
    Libro("hay un dinosaurio en mi sopa","unknown"),
    Libro("harry poter","unknown")
    ]
    us1 = Usuario("Carlos")
    us2 = Usuario("Pedro")
    caso1(libros,us1)
    caso2(libros,us2)
    caso3(libros,us1,us2)

if __name__ == "__main__":
    main()














            

    