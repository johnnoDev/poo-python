"""
Antes de usar DIP
"""
# class Bombilla:
#     def encender(self):
#         print("Bombilla encendida...")

#     def apagar(self):
#         print("Bombilla apagada...")

# class Interruptor:
#     def __init__(self, bombilla: Bombilla):
#         self.dispositivo = bombilla  # Dependencia directa de una clase concreta

#     def presionar(self, estado: bool):
#         if estado:
#             self.dispositivo.encender()
#         else:
#             self.dispositivo.apagar()

"""
Usando DIP
"""
from abc import ABC, abstractmethod

# Creamos la Abstracción (La Interfaz)
class Conectable(ABC):
    @abstractmethod
    def encender(self):
        pass
    def apagar(self):
        pass

# Creamos las clases de Bajo Nivel (Los detalles)
class Bombilla(Conectable):
    def encender(self):
        return 'Bombilla encendida...'
    def apagar(self):
        return 'Bombilla apagada...'
    
class Ventilador(Conectable):
    def encender(self):
        return 'Ventilador encendido... ventilando, calor conchesumare'
    def apagar(self):
        return 'Ventilador apagado... nooOooo'

# Definimos la Clase de Alto Nivel (No se conoce los detalles, solo la abstracción)
class Interruptor:
    def __init__(self, dispositivo: Conectable):
        self.dispositivo = dispositivo
    
    def operar(self, estado: bool):
        if estado:
            print(self.dispositivo.encender())
        else:
            print(self.dispositivo.apagar())

lampara = Bombilla()
ventilador = Ventilador()

control_lampara = Interruptor(lampara)
control_lampara.operar(True)

control_ventilador = Interruptor(ventilador)
control_ventilador.operar(False)
         