# 1. Definimos la función decoradora
# Recibe como parámetro la función que queremos "decorar" o modificar
def funcion_decoradora(funcion_parametro):

    # 2. Definimos una función interna (wrapper)
    # Usamos *args y **kwargs para que acepte cualquier número y tipo de parámetros
    def funcion_interior(*args, **kwargs):

        # Acciones adicionales que decoran (antes de ejecutar la función original)
        print("Vamos a realizar un cálculo: ")

        # 3. Llamamos a la función original con sus argumentos
        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decoran (después de ejecutar la función original)
        print("Hemos terminado el cálculo")

    # 4. Devolvemos la función interior ya modificada
    return funcion_interior

# --- Aplicación de los decoradores ---

@funcion_decoradora
def suma(num1, num2, num3):
    # Esta función ahora imprimirá los mensajes del decorador cuando se llame
    print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

# Esta función NO está decorada, por lo que se ejecutará de forma normal
def potencia(base, exponente):
    print(pow(base, exponente))

# --- Ejemplos de ejecución ---
# suma(5, 5, 5)   # Mostrará los mensajes de "Vamos a realizar..." y "Hemos terminado..."
# resta(10, 5)    # También mostrará los mensajes
# potencia(2, 3)  # Solo mostrará el resultado (8)