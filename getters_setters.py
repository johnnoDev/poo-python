class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    # Permite leer atributos muy protegidos
    def get_nombre(self):
        return self.__nombre

        


johnny = Persona('Johnny')
print(johnny.get_nombre())