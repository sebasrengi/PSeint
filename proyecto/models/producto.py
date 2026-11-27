class ProductoCosmetico:
    def __init__(self, id_cosmetico, nombre, marca, categoria, precio, stock):
        self.id_cosmetico = id_cosmetico
        self.nombre = nombre
        self.marca = marca
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def es_stock_bajo(self):
        return self.stock <= 10