class Volador:
    def mover(self):
        print('Estoy volando por el aire')

class Nadador:
    def mover(self):
        print('Estoy nadando en el agua')

# Cramos una clase 'Pato' que hereda de ambas
class Pato(Volador, Nadador):
    pass

mi_pato = Pato()
mi_pato.mover()
# print(Pato.mro())

# MRO