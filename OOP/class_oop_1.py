class Product:
    def __init__(self, name, price): # Constructor method
        self.name = name
        self.price = price

    def discount(self, percentage):
        return self.price * (1 - percentage/100)
    
    def details(self):
        return f'{self.name} costs {self.price}'

    def __str__(self): # Magic method
        return f'{self.name} costs {self.price}'
    

# Creating object of class Product
product_1 = Product("Book", 100)
product_2 = Product("Khata", 200)

# Accessing the attributes of the object
print(product_1)
print(f"{product_1.name} of Price {product_1.price} and Price after discount {product_1.discount(10)}.")
print(f"{product_2.name} of Price: {product_2.price} TK and Price after discount: {product_2.discount(20)} TK.")

# Accessing the methods of the object
print(product_1.details())