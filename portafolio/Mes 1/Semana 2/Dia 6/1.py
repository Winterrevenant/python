class Carta:
    def __init__(self,palo,figura,valor):
        self.palo = palo
        self.figura = figura
        self.valor = valor


class Baraja:
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
            print(f"{i.figura} {i.palo}",end=" ")

def crear_baraja():
    palos = ["Corazones","Picas","Treboles","Diamantes"]
    bar1=Baraja()
    for i in palos:
        bar1.crear_cartas(i)
    bar1.mostrar_cartas()
    return bar1

def main():
    crear_baraja()

if __name__ == "__main__":
    main()