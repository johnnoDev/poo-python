
def big_function(*args, **kwargs):
    return f'{args}\n{kwargs}'

# *args captura los argumentos y los agrupa en una tupla
print(big_function(1,2,3,'Hola'))

print()

# **kwargs captura los argumentos de clave-valor y los agrupa en un diccionario
print(big_function(parametro1='Zaulo gay', parametro2='añañin'))