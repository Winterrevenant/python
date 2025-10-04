import random

class Carta:
    """Clase que simula una carta"""
    def __init__(self,palo,figura,valor):
        self.palo = palo
        self.figura = figura
        self.valor = valor


class Baraja:
    """Clase que sirve para crear una baraja de poker"""
    def __init__(self):
        self.baraja=[]

    def crear_cartas(self,palo):
        for i in range(2,11):
            self.baraja.append(Carta(palo,i,i))
        self.baraja.append(Carta(palo,"A",(1,11)))
        self.baraja.append(Carta(palo,"J",10))
        self.baraja.append(Carta(palo,"K",10))
        self.baraja.append(Carta(palo,"Q",10))
    
    def mostrar_cartas(self):
        for i in self.baraja:
            print(f"{i.figura} {i.palo} ({i.valor})", end=" ")
        print("-"*50)
    
    def mezclar(self):
        random.shuffle(self.baraja)
    
    def repartir(self):
        carta = self.baraja[0:1]
        del(self.baraja[0:1])
        return carta
    
class Jugador:
    def __init__(self,nombre,mano):
        self.nombre = nombre
        mano = []

def crear_baraja():
    palos = ["Corazones","Picas","Treboles","Diamantes"]
    bar1=Baraja()
    for i in palos:
        bar1.crear_cartas(i)
    bar1.mezclar()
    bar1.mostrar_cartas()
    bar1.repartir()
    bar1.mostrar_cartas()
    return bar1

def main():
    crear_baraja()
    

if __name__ == "__main__":
    main()