class Producto:
    productos = []
    def __init__(self, nombre, precio, stock):
        self.nombre =  nombre
        self.precio = precio
        self.stock = stock

    def vender_producto(self, nombre, cantidad):
        if self.stock > self.cantidad:
            self.stock -= self.cantidad
            print('Venta realizada')
        else:
            print('Stock insuficiente')





p = Producto()

p.vender_producto("Laptop", 3)
p.vender_producto("Laptop", 10)
p.vender_producto("Mouse", 1)

