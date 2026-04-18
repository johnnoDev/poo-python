class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir_informacion(self):
        return f"""Datos de la persona: \n{self.nombre}\n{self.edad}
        """

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir_grado(self):
        return f'El estudiante está en el siguiente grado: {self.grado}'


estudiante1 = Estudiante('Jonathan', 20, '10mo')

print(estudiante1.imprimir_informacion())
print(estudiante1.imprimir_grado())