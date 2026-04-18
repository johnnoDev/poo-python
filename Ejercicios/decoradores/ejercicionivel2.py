def decorador(funcion):
    def envoltura(self, *args, **kwargs):
        print('Antes de la función')
        funcion(self, *args, **kwargs)
        print('Después de la función')
    return envoltura

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @decorador
    def saludo(self):
        print(f'El usuario {self.nombre} está ejecutando un método')

usuario1 = Usuario('Johnny')
usuario1.saludo()