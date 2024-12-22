class Library:
    # def __init__(self, name, books):
    #     self.name = name
    #     self.books = books

    # def display_books(self):
    #     print(f"Books available in {self.name} library:")
    #     for book in self.books:
    #         print(book)

    # def lend_book(self, book_name):
    #     if book_name in self.books:
    #         print(f"{book_name} is available. You can take it.")
    #         self.books.remove(book_name)
    #     else:
    #         print(f"Sorry, {book_name} is not available.")

    # def add_book(self, book_name):
    #     self.books.append(book_name)
    #     print(f"{book_name} has been added to the library.")

    def __init__(self):
        self.books_list = [] # List to store the books

    def book_add(self, book_name):
        self.books_list.append(book_name)
        print(f"{book_name} has been added to the library.")

    def book_remove(self, book_name):
        # if book_name in self.books_list:
        #     self.books_list.remove(book_name)
        #     print(f"{book_name} has been removed from the library.")
        # else:
        #     print(f"Sorry, {book_name} is not available.")

        for book in self.books_list:
            if book == book_name:
                self.books_list.remove(book)
                print(f"{book_name} has been removed from the library.")
                break
            else:
                print(f"Sorry, {book_name} is not available.")
    
    def book_list_show(self):
        # print("Books available in the library:")
        # for book in self.books_list:
        #     print(book)
        
        if not self.books_list:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books_list:
                print(f"- {book.book_name}, by {book.author_name} - {book.price}")

class Book:
    def __init__(self, book_name, author_name, price):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price

# Library class object
my_library = Library()
book_1 = "Some Book"
book_1 = Book("Python Programming", "John Doe", 500)
book_2 = Book("Java Programming", "Jane Doe", 600)

my_library.book_add(book_1)
my_library.book_add(book_2)

my_library.book_list_show()

my_library.book_remove(book_1)
my_library.book_list_show()