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

    def eliminar_datos_por_valor(self,valor):
        #verificando que el valor no sea la cabeza
        while self.cabeza and self.cabeza.valor ==valor:
            self.cabeza=self.cabeza.siguiente
        actual=self.cabeza
        while actual and actual.siguiente:
            if actual.siguiente.valor==valor:
                actual.siguiente=actual.siguiente.siguiente
            else:
                actual=actual.siguiente

        
lista=ListaEnlazada()
lista.insertar(1)
lista.insertar(4)
lista.insertar(1)
lista.insertar(4)
lista.insertar(2)
lista.insertar(4)
lista.insertar(3)
lista.insertar(4)
lista.insertar(4)
lista.insertar(4)

lista.eliminar_datos_por_valor(4)
lista.eliminar_datos_por_valor(1)


lista.mostrar()
    