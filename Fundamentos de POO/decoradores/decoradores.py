def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a la función')
        funcion()
        print('Después de llamar a la función')
    return funcion_modificada

# def saludo():
#     print('Hola esto es un saludo')

# saludo_modificado = decorador(saludo)
# saludo_modificado()

# Lo mismo que lo de acá:
@decorador
def saludo():
    print('Hola que tal')

saludo()