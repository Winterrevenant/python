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
            print(actual.valor,end=" -> ")
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
            
        
lista=ListaEnlazada()


lista.insertar(1)
lista.insertar(2)
lista.insertar(2)
lista.insertar(3)
lista.insertar_final(5)
lista.mostrar()

def clonar_lista(lista_original):
    lista_clonada=ListaEnlazada()
    actual=lista_original.cabeza

    while actual:
        
        lista_clonada.insertar_final(actual.valor)
        actual=actual.siguiente
    return lista_clonada


lista2=clonar_lista(lista)
lista2.mostrar()