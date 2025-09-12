from typing import Optional
class Nodo:
    def __init__(self,valor):

        self.valor=valor
        self.siguiente: Optional['Nodo'] = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza=None        
    def insertar(self,valor):
        nuevo_nodo=Nodo(valor)
        nuevo_nodo.siguiente=self.cabeza
        self.cabeza = nuevo_nodo
    def mostrar(self):
        actual=self.cabeza
        while actual:
            print(actual.valor,end=" -> ")
            actual = actual.siguiente
        print("None")
    def insertar_posicion(self,valor,index):
        
        
        nuevo_nodo=Nodo(valor)
        if index==0:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza=nuevo_nodo
            return
        
        actual=self.cabeza
        contador=0
        while actual and contador <index -1:
            actual=actual.siguiente
            contador+=1

        if not actual:
            print("Posicion fuera de rango")
            return
        nuevo_nodo.siguiente=actual.siguiente
        actual.siguiente=nuevo_nodo
            


lista1=ListaEnlazada()
lista1.insertar(6)
lista1.insertar(5)
lista1.insertar(4)
lista1.insertar(2)
lista1.insertar(1)
lista1.insertar_posicion("x",1)
lista1.mostrar()

