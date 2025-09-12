class Nodo:
    def __init__(self,valor):
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

def uni_ordenar(x,z):
    valores=[]
    actual1=x.cabeza
    actual2=z.cabeza
    while actual1:
        valores.append(actual1.valor)
        actual1=actual1.siguiente

    while actual2:
        valores.append(actual2.valor)
        actual2=actual2.siguiente
    valores.sort()
    
    lista_ordenada=ListaEnlazada()
    for i in valores:
        lista_ordenada.insertar_final(i)
    return lista_ordenada
    
lista3=uni_ordenar(lista1,lista2)
lista3.mostrar()
    
