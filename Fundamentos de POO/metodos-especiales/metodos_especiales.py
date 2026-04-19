class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'

    # 'otro' hace referencia al otro valor que deseamos sumarle
    def __add__(self, otro):
        suma_edad = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, suma_edad)

johnny = Persona("Johnny", 20)
carlos = Persona("Carlos", 30)
nueva_persona = carlos + johnny

print(nueva_persona.nombre)


"""""
Descomentar para probar el método especial '__repr__'
"""
# repr = repr(persona1)
# resultado = eval(repr)
# print(resultado)