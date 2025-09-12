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
    def invertir(self):
        anterior=None
        actual=self.cabeza
        

        while actual:
            siguiente=actual.siguiente
            actual.siguiente=anterior
            anterior=actual
            actual=siguiente
        self.cabeza=anterior  
            
            
        
        print("None")    
            
           
        
lista=ListaEnlazada()

lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)

lista.invertir()
lista.mostrar()

