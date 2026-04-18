"""
Ejercicio 2: El Portero de Datos (Validación)
Objetivo: Implementar un decorador que verifique que los argumentos pasados a un método de clase sean del tipo correcto antes de procesarlos.

Instrucciones:

Crea una clase llamada CuentaBancaria con un atributo saldo.

Define un decorador llamado validar_numero que compruebe si el valor ingresado es un entero o flotante y si es mayor a cero.

Si el valor no es válido, debe imprimir un error; de lo contrario, debe permitir que el método se ejecute.

Aplica este decorador a un método depositar(cantidad).
"""

def validar_numero(function):
    def wrapper(self, *args, **kwargs):
        cantidad = args[0]
        if isinstance(cantidad, (int, float)) and cantidad > 0:
            return function(self, *args, **kwargs)
        else:
            return 'Es un valor negativo. Inténtalo de nuevo.'
    return wrapper

class CuentaBancaria:
    def __init__(self):
        self.saldo = 1000

    @validar_numero
    def depositar(self, cantidad):
        self.saldo += cantidad
        return f'Deposito exitoso. El nuevo saldo es el siguiente: {self.saldo}'

cuenta = CuentaBancaria()
print(cuenta.depositar(100))