def decorador(funcion):
    def envoltura(self, *args, **kwargs):
        print('Antes de la función')
        funcion(self, *args, **kwargs)
        print('Después de la función')
    return envoltura

class Mensaje:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    @decorador
    def obtener_mensaje(self):
        print(f'{self.mensaje.upper()}')

mensaje1 = Mensaje("hola mundo")
mensaje1.obtener_mensaje()