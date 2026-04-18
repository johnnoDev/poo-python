import time  # Importamos el módulo para medir tiempo


# 🔹 DECORADOR
def medir_tiempo(funcion):
    # 'funcion' es el método que vamos a decorar (sumar)

    def envoltura(*args, **kwargs):
        # *args → recibe todos los argumentos por posición (incluye self)
        # **kwargs → recibe argumentos con nombre

        inicio = time.time()  
        # Guardamos el tiempo antes de ejecutar la función

        resultado = funcion(*args, **kwargs)
        # Ejecutamos la función original (sumar)
        # IMPORTANTE: usamos *args y **kwargs para pasar todo correctamente
        # Guardamos el resultado (por ejemplo: 5 + 10 = 15)

        fin = time.time()  
        # Guardamos el tiempo después de ejecutar la función

        print(f"Tiempo de ejecución: {fin - inicio} segundos")
        # Calculamos cuánto tiempo pasó

        return resultado  
        # Devolvemos el resultado original para no romper la función

    return envoltura  
    # Retornamos la nueva función (la que reemplaza a 'sumar')


# 🔹 CLASE
class Calculadora:

    @medir_tiempo
    # Aquí aplicamos el decorador al método 'sumar'
    # Python hace esto internamente:
    # sumar = medir_tiempo(sumar)

    def sumar(self, a, b):
        # self → referencia al objeto (calc)
        # a, b → números a sumar

        return a + b
        # Retorna el resultado de la suma


# 🔹 PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Esto asegura que el código se ejecute solo si corres este archivo directamente

    calc = Calculadora()
    # Creamos un objeto de la clase

    resultado = calc.sumar(5, 10)
    # Llamamos al método

    # 🔥 IMPORTANTE: en realidad se ejecuta así:
    # envoltura(calc, 5, 10)

    print("Resultado:", resultado)
    # Imprime el resultado final