class Auto:
    def __init__(self):
        self._estado = 'apagado'

    def encender(self):
        if self._estado == 'apagado':
            self._estado = 'encendido'
            print('El auto está encendido')

    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
            print('Conduciendo...')

auto = Auto()
# auto.encender()
auto.conducir()