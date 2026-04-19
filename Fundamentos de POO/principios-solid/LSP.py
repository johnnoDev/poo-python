# class Ave:
#     def volar(self):
#         return 'Estoy volando'

# class Pinguino(Ave):
#     pass # <-- Eliminar esta línea
#     # def volar(self):
#     #     return 'No puedo volar'
    
# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))


class Ave:
    def comer(self):
        return 'Estoy comiendo...'

class AveVoladora(Ave):
    def volar(self):
        return 'Estoy volando...'

class AveNoVoladora(Ave):
    def caminar(self):
        return 'Camino por el suelo...'
    
class Pinguino(Ave):
    def nadar(self):
        return 'Estoy nadando...'
    
def iniciar_vuelo_grupal(aves: list[AveVoladora]):
    for ave in aves:
        print(ave.volar())

solo_voladores = [AveVoladora(), AveVoladora()]
iniciar_vuelo_grupal(solo_voladores)

otras_aves = [Pinguino(), Pinguino()]
iniciar_vuelo_grupal(otras_aves)