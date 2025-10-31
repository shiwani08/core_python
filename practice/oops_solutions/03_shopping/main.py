from product import Product
from cart import Cart

def main():
    product = Product("Laptop", 1500)
    print(f"Product Name: {product.get_name()}")
    print(f"Product Price: ${product.get_price()}")

    cart = Cart()
    cart.add_item("Laptop")
    cart.add_item("Mouse")
    print("Cart Items:", cart.view_cart())
    cart.remove_item("Mouse")
    print("Cart Items:", cart.view_cart())

main()
