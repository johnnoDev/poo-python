"""
Crear un juego de fusión.

El juego consiste en crear personajes un juego y que esos personajes se puedan fusionar para formar personajes más poderosos que tengan más poder...

Para ello deberemos cambiar el comportamiento del operador “+” para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas.

una posible formula es: el promedio de las habilidades de ambos, al cuadrado!
"""

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f'{self.nombre}, Estadísticas(Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'

    def __add__(self, otropj):
        nuevo_personaje = self.nombre + otropj.nombre
        nueva_fuerza = round(((self.fuerza + otropj.fuerza)/2)**2)
        nueva_velocidad = round(((self.velocidad + otropj.velocidad)/2)**2)
        return Personaje(nuevo_personaje, nueva_fuerza, nueva_velocidad)

goku = Personaje('Goku', 1000, 560)
vegeta = Personaje('Vegeta', 950, 540)
gogeta = goku + vegeta


print(goku)
print(gogeta)