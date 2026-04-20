
class Persona:
    especie = 'Humano'
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie

    @staticmethod
    def es_mayor_edad(edad):
        return edad >= 18
    
    def __str__(self):
        return f'La especie de {self.nombre} es: {self.especie}'

persona = Persona('Carlos', 20)
persona2 = Persona('Juan', 20)
persona3 = Persona('Pedro', 20)
persona4 = Persona('Jonnathan', 20)
print(persona)
print(persona2)
Persona.cambiar_especie('Reptiliano')
print(persona3)
print(persona4)

print(Persona.es_mayor_edad(20))
print(Persona.es_mayor_edad(persona4.edad))
