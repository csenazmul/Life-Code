# Create Class Book Management System (Name, Author, Price, Discount, Stock)

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
    
    def details(self):
        return f"Book Name: {self.name}, Author: {self.author}, Price: {self.price}. TK"
    
# Create object of class Book
book_1 = Book("Python", "Guido Van Rossum", 1000)
book_2 = Book("Java", "James Gosling", 1500)

# method of the object
print(book_1.details())
print(book_2.details())