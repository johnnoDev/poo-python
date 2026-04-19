"""
Algoritmo antes de usar ISP
"""
# from abc import ABC, abstractmethod
# class Trabajador(ABC):
    
#     @abstractmethod
#     def comer(self):
#         pass
    
#     @abstractmethod
#     def trabajar(self):
#         pass

#     @abstractmethod
#     def dormir(self):
#         pass

# class Humano(Trabajador):
#     def comer(self):
#         return 'El humano está comiendo...'
    
#     def trabajar(self):
#         return 'El humano está camellando de lo lindo...'

#     def dormir(self):
#         return 'El humano está durmiendo...'
    
# class Robot(Trabajador):
#     def comer(self): # <-- Mala práctica
#         pass

#     def trabajar(self):
#         return 'El humano está camellando de lo lindo...'
    
#     def dormir(self): # <-- Mala práctica
#         pass 
  
# humano = Humano()
# robot = Robot()
# print(humano.comer())
"""
Usando ISP
"""
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Humano(Trabajador, Durmiente, Comedor):
    def trabajar(self):
        return 'El humano está camellando de lo lindo...'
    def dormir(self):
        return 'EL humano se está pegando una ruca...(déjalo dormir, ctm)'
    def comer(self):
        return 'El humano está comiendo...'
    
class Robot(Trabajador):
    def trabajar(self):
        return 'El robot está trabajando...'
    def __str__(self):
        return self.trabajar()
    
humano = Humano()
robot = Robot()
print(humano.trabajar())
print(robot)