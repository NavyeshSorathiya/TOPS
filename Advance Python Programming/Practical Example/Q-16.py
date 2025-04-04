# Write a Python program to show hierarchical inheritance.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_details(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")


class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def show_details(self):
        super().show_details()
        print(f"Brand: {self.brand}")
        print(f"Category: Electronics")


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def show_details(self):
        super().show_details()
        print(f"Size: {self.size}")
        print(f"Category: Clothing")


class Books(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def show_details(self):
        super().show_details()
        print(f"Author: {self.author}")
        print(f"Category: Books")

class Delivery:
    def __init__(self, product_name):
        self.product_name = product_name

    def standard_delivery(self):
        print(f"Standard delivery for {self.product_name}: 5-7 days")

    def express_delivery(self):
        print(f"Express delivery for {self.product_name}: 1-3 days")

electronics_product = Electronics("Smartphone", 699, "Apple")
clothing_product = Clothing("T-shirt", 19.99, "M")
book_product = Books("Python Programming", 29.99, "John Doe")

electronics_product.show_details()
print()
clothing_product.show_details()
print()
book_product.show_details()

electronics_delivery = Delivery(electronics_product.name)
clothing_delivery = Delivery(clothing_product.name)
book_delivery = Delivery(book_product.name)

print()
electronics_delivery.standard_delivery()
electronics_delivery.express_delivery()

print()
clothing_delivery.standard_delivery()
clothing_delivery.express_delivery()

print()
book_delivery.standard_delivery()
book_delivery.express_delivery()