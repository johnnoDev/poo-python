def decorador(func):
    def envoltura(*args, **kargs):
        print('Antes de la función')
        resultado = func(*args, **kargs)
        print('Después de la función')
        return resultado
    return envoltura

@decorador
def mi_funcion():
    print('Esta es mi función')

mi_funcion()