class Nodo:
    def __init__(self,valor=0):
        self.valor=valor
        self.siguiente=None

class ListaEnlazada:
    def __init__(self):
        self.cabeza=None

    def insertar(self,valor):
        nuevo_nodo=Nodo(valor)
        nuevo_nodo.siguiente=self.cabeza
        self.cabeza=nuevo_nodo
    def mostrar(self):
        actual=self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual=actual.siguiente
        print("None")
    def insertar_final(self,valor):
        nuevo_nodo=Nodo(valor)
        actual=self.cabeza
        if  self.cabeza is None:
            self.cabeza=nuevo_nodo
        else:
            while actual.siguiente:
                
                actual=actual.siguiente
            actual.siguiente=nuevo_nodo



lista1=ListaEnlazada()

lista1.insertar(4)
lista1.insertar(2)
lista1.insertar(1)

lista2=ListaEnlazada()
lista2.insertar(1)
lista2.insertar(4)
lista2.insertar(3)
lista2.insertar(1)


def unir_ordenar(x,y):
    dummy=Nodo(0)
    tail=dummy

    while x and y:
        if x.cabeza.valor < y.cabeza.valor:
            
            tail.siguiente=x.cabeza
            x=x.cabeza.siguiente
        else:
            tail.siguiente=y.cabeza
            y=y.cabeza.siguiente
        tail=tail.siguiente
    
    tail.siguiente= lista1 if lista1 else lista2
    return dummy.siguiente

   
z=unir_ordenar(lista1,lista2)
print(z)
        
