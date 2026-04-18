class Vehiculo:
    def __init__(self, marca, modelo, precio_base):
        self.marca = marca
        self.modelo = modelo
        self.precio_base = precio_base

    def obtener_info(self):
        return f"""DATOS DEL VEHÍCULO \n
        Marca: {self.marca} \n
        Modelo: {self.modelo} \n
        Precio Base: {self.precio_base} \n
        """
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio_base, puertas):
        super().__init__(marca, modelo, precio_base)
        self.puertas = puertas
    
    def calcular_impuesto(self):
        return self.precio_base * 0.10

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio_base, cilindrada):
        super().__init__(marca, modelo, precio_base)
        self.cilindrada = cilindrada
    
    def calcular_impuesto(self):
        return self.precio_base * 0.05

auto1 = Auto('Toyota', 'Corolla', 25000, '4 puertas')
moto1 = Moto('Yamaha', 'R6', 12000, '600cc')

print(f"{auto1.obtener_info()}\n Precio Final: {int(auto1.precio_base) + int(auto1.calcular_impuesto())}")
print(f"{moto1.obtener_info()}\n Precio Final: {int(moto1.precio_base) + int(moto1.calcular_impuesto())}")
