"""
Antes de aplicar el SRP
"""
# class Auto:
#     def __init__(self):
#         # Definimos los atributos estáticos
#         self.posicion = 0
#         self.combustible = 100

#     def mover(self, distancia):
#         if self.combustible >= distancia / 2:
#             self.posicion += distancia
#             self.combustible -= distancia / 2
#         else:
#             print("No hay suficiente combustible")

#     def agregar_combustible(self, cantidad):
#         self.combustible += cantidad

#     def obtener_combustible(self):
#         return self.combustible 
    
"""
Aplicando SRP
"""

class Auto:
    def __init__(self, tanque):
        self.posicion = 0 # atributo estático
        self.tanque = tanque # atributo de instancia

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print('Moviendo el auto...')
        else:
            print("No hay suficiente combustible")


class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible 

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

tanque = TanqueDeCombustible()
auto = Auto(tanque)
print(auto.posicion)
auto.mover(10)
print(auto.posicion)
auto.mover(30)
print(auto.posicion)
auto.mover(50)
print(auto.posicion)
auto.mover(100)
print(auto.posicion)
auto.mover(100)


