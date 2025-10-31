class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

product = Product("Laptop",1500)
print(f"Product Name: {product.get_name()}")
print(f"Product Price: ${product.get_price()}")