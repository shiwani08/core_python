class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def view_cart(self):
        return self.items
    
cart = Cart()
cart.add_item("Laptop")
cart.add_item("Mouse")
print("Cart Items:", cart.view_cart())
cart.remove_item("Mouse")
print("Cart Items:", cart.view_cart())