class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
class ListaEnlazada:
    def __init__(self):
        self.cabeza=None
    def agregar(self,dato):
        nuevo_nodo=Nodo(dato)
        nuevo_nodo.siguiente=self.cabeza
        self.cabeza=nuevo_nodo
    def mostrar(self):
        actual=self.cabeza
        while actual:
            print(actual.dato,end=" -> ")
            actual=actual.siguiente
        print("None")
    def agregar_al_final(self,dato):
        nuevo=Nodo(dato)
        if self.cabeza is None:
            self.cabeza=nuevo
        else:
            actual=self.cabeza
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente=nuevo
    def buscar(self,valor):
        actual=self.cabeza
        while actual:
            if actual.dato==valor:
                return True
            actual = actual.siguiente
        return False
    def eliminar(self,valor):
        actual=self.cabeza
        anterior=None
        while actual:
            if actual.dato == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza=actual.siguiente
                return True
            anterior = actual
            actual=actual.siguiente
        return False


lista=ListaEnlazada()
lista.agregar("manzana")
lista.agregar("pera")
lista.agregar("uva")
lista.agregar_al_final("final")
print("¿Está 'banana'?", lista.buscar("final"))
lista.eliminar("final")
lista.mostrar()