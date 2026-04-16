class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    # Permite leer atributos muy protegidos
    def get_nombre(self):
        return self.__nombre

    # Permite modificar/escribir atributos muy protegidos
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        return nuevo_nombre


johnny = Persona('Johnny')
print(johnny.get_nombre())

caiza = Persona('Caiza')
print(caiza.set_nombre('Zaulo'))
