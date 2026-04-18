class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"

mi_objeto = MiClase()
print(mi_objeto._atributo_privado) # Sí se imprime

class OtraClase:
    def __init__(self):
        # Propiedad 'Muy privado'   
        self.__atributo_privado = "Valor"
    def __hablar(self): # Método privado
        print('Hola')

otro_objeto = OtraClase()
print(otro_objeto.__atributo_privado)