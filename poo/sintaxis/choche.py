class Coche:
    def __init__(self,marca,modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año

    def encender(self):
        print(f"El Coche {self.marca} esta encendido")
    def __str__(self):
        return f"Coche Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"


coche1=Coche("Ford","Unknown","2003")

print(coche1)
coche1.encender()