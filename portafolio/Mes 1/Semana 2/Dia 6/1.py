class Carta:
    def __init__(self,nombre,palo,valor):
        self.nombre = nombre
        self.palo = palo
        self.valor = valor


class Baraja:
    def __init__(self):
        self.baraja=[]

    def corazones(self):
        for i in range(2,11):
            self.baraja.append(Carta("Corazones",i,i))
        self.baraja.append(Carta("Corazones","A",(1,11)))
        self.baraja.append(Carta("Corazones","J",10))
        self.baraja.append(Carta("Corazones","K",10))
        self.baraja.append(Carta("Corazones","Q",10))
    
    def picas(self):
        for i in range(2,11):
            self.baraja.append(Carta("Picas",i,i))
        self.baraja.append(Carta("Picas","A",(1,11)))
        self.baraja.append(Carta("Picas","J",10))
        self.baraja.append(Carta("Picas","K",10))
        self.baraja.append(Carta("Picas","Q",10))

    def treboles(self):
        for i in range(2,11):
            self.baraja.append(Carta("Treboles",i,i))
        self.baraja.append(Carta("Treboles","A",(1,11)))
        self.baraja.append(Carta("Treboles","J",10))
        self.baraja.append(Carta("Treboles","K",10))
        self.baraja.append(Carta("Treboles","Q",10))

    def diamantes(self):
        for i in range(2,11):
            self.baraja.append(Carta("Diamantes",i,i))
        self.baraja.append(Carta("Diamantes","A",(1,11)))
        self.baraja.append(Carta("Diamantes","J",10))
        self.baraja.append(Carta("Diamantes","K",10))
        self.baraja.append(Carta("Diamantes","Q",10))


def crear_baraja():
    bar1=Baraja()
    bar1.corazones()
    bar1.diamantes()
    bar1.treboles()
    bar1.picas()
    print(len(bar1.baraja))
    return bar1

def main():
    crear_baraja()

if __name__ == "__main__":
    main()