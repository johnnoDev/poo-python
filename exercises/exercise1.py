class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        return f'El estudiante {self.nombre} está estudiando'

estudiante1 = Estudiante('Johnny', 20, '10mo Grado')

print(estudiante1.nombre)
print(estudiante1.estudiar())