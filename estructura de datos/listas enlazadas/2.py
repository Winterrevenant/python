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

    def insertar_al_final(self,valor):
        nuevo_nodo=Nodo(valor)
        if not self.cabeza:
            self.cabeza=nuevo_nodo
            return
        actual=self.cabeza
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nuevo_nodo
    def buscar(self,valor):
        actual=self.cabeza
        while actual:
            if actual.valor==valor:
                return True
            actual=actual.siguiente
        return False
    def eliminar(self,valor):
        # si no hay nada en la lista regresa none
        if not self.cabeza:
            return
        #verifica si el valor esta en la cabeza
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        # Buscar el nodo anterior al que contiene el valor a eliminar
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente


lista1=ListaEnlazada()
lista2=ListaEnlazada()
lista3=ListaEnlazada()
lista1.insertar(4)
lista1.insertar(2)
lista1.insertar(1)

lista2.insertar(4)
lista2.insertar(3)
lista2.insertar(1)

x=lista1.cabeza.valor

while x:
    if x<lista1.cabeza.siguiente.valor:
        x=lista1.cabeza.siguiente.valor
        break
    else:
        lista3.insertar(x.valor)