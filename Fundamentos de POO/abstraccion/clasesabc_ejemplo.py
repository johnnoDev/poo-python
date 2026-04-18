from abc import ABC, abstractmethod

# Definimos la clase abstracta
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

# Clase concreta que hereda de la abstracta
class Rectangulo(Forma):
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    # Implementación obligatoria de los métodos abstractos
    def area(self):
        return self.ancho * self.altura

    def perimetro(self):
        return 2 * (self.ancho + self.altura)
    
# rect = Forma() # Esto daría error
rect = Rectangulo(5, 10)
print(rect.area())
