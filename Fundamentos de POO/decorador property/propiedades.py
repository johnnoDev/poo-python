class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    # Comportamiento igual al getter
    @property
    def nombre(self):
        return self.__nombre
    
    # Comportamiento igual el setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Decorador para eliminar propiedades
    @nombre.deleter
    def nombre(self):
        del self.__nombre

persona = Persona('Johnny')
print(persona.nombre)

persona.nombre = 'Carlos'
print(persona.nombre)

# del persona.nombre
# print(persona.nombre)