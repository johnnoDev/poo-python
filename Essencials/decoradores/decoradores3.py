def mi_decorador(funcion):
    def envoltura(*args, **kwargs):
        print("Antes del saludo")
        funcion(*args, **kwargs)
        print("Después del saludo")
    return envoltura


class Saludo:

    @mi_decorador
    def decir_hola(self, nombre):
        print(f"Hola {nombre}")


obj = Saludo()
obj.decir_hola("Juan")