class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    def arrancar(self):
        print(f"Encender vehiculo generico")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo,cilindrada):
        super().__init__(marca, modelo)

        self.cilindradra=cilindrada
    def arrancar(self):
        print(f"La motocicleta {self.marca} {self.modelo} ha arrancado")
class Auto(Vehiculo):
    def __init__(self, marca, modelo,puertas):
        super().__init__(marca, modelo)
        self.puertas=puertas
    def arrancar(self):
        super().arrancar()
    


moto1=Motocicleta("yamaha","R6","600cc")
auto1=Auto("Ford","Unknown",4)

moto1.arrancar()
auto1.arrancar()