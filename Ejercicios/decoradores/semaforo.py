 
def decorador(function):
    def envoltura(self,*args, **kwargs):
        print('Haciendo calculo....')
        function(self,*args, **kwargs)
        print('Fin del calculo')
    return envoltura

class Calcularadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @decorador
    def sumar(self):
        print(self.a + self.b)
    @decorador
    def restar(self):
        print(self.a - self.b)
    
calculadora1 = Calcularadora(5, 7)
calculadora1.sumar()