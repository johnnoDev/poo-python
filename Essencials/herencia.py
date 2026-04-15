"""
EJERCICIO DE PROGRAMACIÓN ORIENTADA A OBJETOS: HERENCIA EN PYTHON

OBJETIVO:
Implementar un sistema básico de gestión de personas utilizando el concepto 
de herencia para reutilizar código y establecer jerarquías entre clases.

REQUERIMIENTOS:
1. Clase Base (Persona): 
   - Debe tener los atributos: nombre, edad y nacionalidad.
   - Debe incluir un método llamado 'hablar' que imprima un mensaje por consola.

2. Clases Hijas (Herencia):
   - Empleado: Hereda de Persona. Añade los atributos específicos 'trabajo' 
     y 'salario'.
   - Estudiante: Hereda de Persona. Añade los atributos específicos 'notas' 
     y 'universidad'.
   
3. Implementación:
   - Utilizar el método super().__init__() en las clases hijas para inicializar 
     los atributos heredados de la clase padre.
   - Realizar una instancia de la clase Empleado con datos de prueba.
"""


class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        return 'Hablando...'

# Herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

empleado1 = Empleado('Juan', 25, 'Ecuatoriano', 'DBA', 10000)

print(f"""DATOS DEL EMPLEADO \n \n
    Nombre: {empleado1.nombre}\n
    Edad: {empleado1.edad}\n
    Nacionalidad: {empleado1.nacionalidad}\n
    Notas: {empleado1.trabajo}\n
    Universidad: {empleado1.salario}
""")


