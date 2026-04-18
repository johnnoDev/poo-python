class celulares:
    def __init__(self, marca, memoria, ram, camara, procesador):
        self.marca = marca
        self.memoria = memoria
        self.ram = ram
        self.camara = camara
        self.procesador = procesador

    def especificaciones(self):
        return f"La marca {self.marca} tiene un celular con unas especificaciones que tiene las siguientes cosas: {self.memoria}GB, {self.ram}GB de RAM y el procesador {self.procesador}."

class xiaomi(celulares):
    def __init__(self, marca, memoria, ram, camara, procesador):
        super().__init__(marca, memoria, ram, camara, procesador)

class iphone(celulares):
    def __init__(self, marca, memoria, ram, camara, procesador):
        super().__init__(marca, memoria, ram, camara, procesador)

class samsung(celulares):
    def __init__(self, marca, memoria, ram, camara, procesador, novedads):
        super().__init__(marca, memoria, ram, camara, procesador)
        self.novedads = novedads

    def nsamsung(self):
        return f"La novedad de Samsung es que su celular es {self.novedads}."

xiaomi1 = xiaomi("Xiaomi", 128, 16, 128, "Helio G99")
iphone1 = iphone("iPhone", 256, 8, 56, "A15")
samsung1 = samsung("Samsung", 360, 12, 49, "Snapdragon", "plegable")


ofertas_xiaomi = ("Redmi Note 12", "Poco X5 Pro", "Xiaomi 13 Lite") 
ofertas_iphone = ("iPhone 11", "iPhone 13 Mini", "iPhone 14")
ofertas_samsung = ("Galaxy A54", "Galaxy S21 FE", "Galaxy Z Flip 3")   

print("\n" + "*"*40)
print(" OFERTAS ESPECIALES DE LA SEMANA ")
print("*"*40)

print("\n Ofertas Xiaomi:")
for modelo in ofertas_xiaomi:
    print(f" - {modelo}")

print("\n📱 Ofertas iPhone:")
for modelo in ofertas_iphone:
    print(f" - {modelo}")

print("\n📱 Ofertas Samsung:")
for modelo in ofertas_samsung:
    print(f" - {modelo}")

print("\n" + "*"*40)


ver_menu = input("\n¿Deseas ver las especificaciones detalladas de nuestros modelos principales? (s/n): ").lower()

if ver_menu == 's':
    while True:
        print("\n" + "="*30)
        print(" MENÚ DE CELULARES ")
        print("="*30)
        print("1. Ver especificaciones de Xiaomi 10")
        print("2. Ver especificaciones de iPhone 13 ")
        print("3. Ver especificaciones de Samsung s21 ")
        print("4. Ver característica especial de Samsung")
        print("5. Salir del programa")
        print("="*30)
        
        opcion = input("Elige una opción (1-5): ")
        print() 

        if opcion == "1":
            print(xiaomi1.especificaciones())
        elif opcion == "2":
            print(iphone1.especificaciones())
        elif opcion == "3":
            print(samsung1.especificaciones())
        elif opcion == "4":
            print( samsung1.nsamsung())
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break 
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 5.")
            continue 
            
        print("\n" + "-"*30)
        volver = input("¿Deseas ver las especificaciones de otros celulares en el menú? (s/n): ").lower()
        
        if volver == "n":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
else:
    print("\n¡Gracias por ver nuestras ofertas! Vuelve pronto.")