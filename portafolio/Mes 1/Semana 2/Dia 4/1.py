class Animal:
    def __init__(self):
        pass

    def hablar(self):
        print("Sonido generico")

class Perro(Animal):
    def hablar(self):

        print("Gua")

class Gato(Animal):
    def hablar(self):
        
        print("Miau")




def main():
   animales = [Perro(),Gato(),Perro()]

   for a in animales:
       a.hablar()


if __name__ == "__main__":
    main()