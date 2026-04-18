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

celulares = [xiaomi1, iphone1, samsung1]

for o in celulares:
    print (o.especificaciones())

print ("============= ofertas ========================")

for ofertas in ofertas_xiaomi:
    print ( ofertas)