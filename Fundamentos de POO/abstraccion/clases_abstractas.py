from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')

""""
Esto daría error por que no es posible instanciar una clase abstracta:
"""    
# persona = Persona('Johnny', 20, 'Masculino') 

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Esto es lo que estoy haciendo: {self.actividad}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f'Estoy trabajando en el siguiente cargo: {self.actividad}')
    

estudiante = Estudiante('Jonathan Caiza', 20, 'No tiene sexo', 'Existir')
trabajador = Trabajador('Zaulo', 20, 'Masculino', 'Perchero del Tuti')

estudiante.presentarse()
estudiante.hacer_actividad()

trabajador.presentarse()
trabajador.hacer_actividad()