# Base class: User (common properties for both customers and sellers)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_user_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


# Product class (represents a product in the system)
class Product:
    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock
    
    def display_product_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price}")
        print(f"Stock Available: {self.stock}")


# Customer class inherits from User (Specific to customers)
class Customer(User):
    def __init__(self, name, email, shipping_address):
        super().__init__(name, email)  # Initialize User class
        self.shipping_address = shipping_address

    def display_customer_info(self):
        self.display_user_info()  # Display info from User class
        print(f"Shipping Address: {self.shipping_address}")


# Seller class inherits from User (Specific to sellers)
class Seller(User):
    def __init__(self, name, email, store_name):
        super().__init__(name, email)  # Initialize User class
        self.store_name = store_name

    def display_seller_info(self):
        self.display_user_info()  # Display info from User class
        print(f"Store Name: {self.store_name}")


# Order class, which will combine information from Customer, Seller, and Product
class Order(Customer, Seller, Product):
    def __init__(self, customer_name, customer_email, shipping_address, seller_name, seller_email, store_name, product_name, price, stock):
        # Initialize Customer
        Customer.__init__(self, customer_name, customer_email, shipping_address)
        
        # Initialize Seller
        Seller.__init__(self, seller_name, seller_email, store_name)
        
        # Initialize Product
        Product.__init__(self, product_name, price, stock)

    def display_order_info(self):
        print("Customer Information:")
        self.display_customer_info()
        print("Seller Information:")
        self.display_seller_info()
        print("Product Information:")
        self.display_product_info()


# Example of creating an Order
order = Order(
    customer_name="John Doe", 
    customer_email="john.doe@example.com", 
    shipping_address="123 Amazon St, City, Country", 
    seller_name="Best Electronics Store", 
    seller_email="beststore@example.com", 
    store_name="BestElectronics", 
    product_name="Smartphone", 
    price=599.99, 
    stock=100
)

# Display the order details
order.display_order_info()
