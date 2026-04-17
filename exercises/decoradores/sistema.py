def decorador(funcion):
    def envoltura(self, *args, **kwargs):
        print('Antes de la función')
        funcion(self, *args, **kwargs)
        print('Después de la función')
    return envoltura
        
class Sistema:
    def __init__(self, autenticado):
        self.autenticado = autenticado
    @decorador
    def ver_datos(self):
        if self.autenticado:
            print('Acceso autorizado')
        else: 
            print("Acceso denegado")

sistema1 = Sistema(False)
sistema1.ver_datos()
