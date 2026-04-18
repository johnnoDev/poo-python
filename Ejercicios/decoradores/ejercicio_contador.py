"""  
Ejercicio 3: El Contador de Instancias (Estado en Decoradores)
Objetivo: Usar un decorador para contar cuántas veces se ha llamado a un método específico en toda la aplicación, independientemente de la instancia.

Instrucciones:

Define un decorador que utilice una variable externa (o un atributo de la función) para llevar la cuenta.

Crea una clase ServicioMensajeria.

Decora el método enviar_mensaje(texto) para que, cada vez que se llame, incremente el contador y muestre: "Mensajes enviados hasta ahora: X".
"""

def decorador_contador(function):
    def wrapper(self, *args, **kwargs):
        wrapper.cuenta += 1
        print(f'Mensajes enviados hasta ahora: {wrapper.cuenta}')
        return function(self, *args, **kwargs)
    wrapper.cuenta = 0 # Inicialización del contador
    return wrapper

class ServicioMensajeria:
    @decorador_contador
    def enviar_mensaje(self, mensaje):
        return f'Mensaje enviado: {mensaje}'

mensaje = ServicioMensajeria()
print(mensaje.enviar_mensaje('Hola'))
print(mensaje.enviar_mensaje('Hola'))
print(mensaje.enviar_mensaje('Hola'))