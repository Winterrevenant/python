class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    def hablar(self):
        print("Hablar")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice Gua")
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice Miau")
        
perro1=Perro("Chispas")
gato1=Gato("Concha")

perro1.hablar()
gato1.hablar()