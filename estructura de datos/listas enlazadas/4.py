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

    def contar(self):
        actual=self.cabeza
        contador=0
        while actual:
            actual=actual.siguiente
            contador+=1
        print(f"Total de nodos: {contador}")

lista=ListaEnlazada()

lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)

lista.contar()

lista.mostrar()