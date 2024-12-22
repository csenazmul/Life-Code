# Library Management System

এই প্রজেক্টটি একটি সরল Python ভিত্তিক **Library Management System** তৈরি করে। এতে দুটি ক্লাস ব্যবহার করা হয়েছে: **Library** এবং **Book**। কোডের প্রতিটি ধাপ নিচে ব্যাখ্যা করা হলো।

---

## Features
- নতুন বই যোগ করার ফিচার।
- বিদ্যমান বই মুছে ফেলার ফিচার।
- লাইব্রেরিতে থাকা সকল বইয়ের তালিকা দেখানোর ফিচার।

---

## Classes

### 1. Library Class
লাইব্রেরির সমস্ত কার্যক্রম পরিচালনার জন্য এই ক্লাসটি তৈরি করা হয়েছে। নিচের ফাংশনগুলো অন্তর্ভুক্ত রয়েছে:

#### `__init__()`
লাইব্রেরির জন্য একটি খালি বইয়ের তালিকা তৈরি করে।
```python
def __init__(self):
    self.books_list = []  # List to store the books
```

#### `book_add(book_name)`
নতুন বই লাইব্রেরিতে যোগ করার জন্য ব্যবহৃত হয়।
```python
def book_add(self, book_name):
    self.books_list.append(book_name)
    print(f"{book_name} has been added to the library.")
```


#### `book_remove(book_name)`

লাইব্রেরি থেকে কোনো বই মুছে ফেলার জন্য ব্যবহৃত হয়।
```python
def book_remove(self, book_name):
    for book in self.books_list:
        if book == book_name:
            self.books_list.remove(book)
            print(f"{book_name} has been removed from the library.")
            break
        else:
            print(f"Sorry, {book_name} is not available.")
```

book_list_show()

লাইব্রেরিতে বর্তমানে উপলব্ধ বইগুলোর তালিকা দেখায়।
```python
def book_list_show(self):
    if not self.books_list:
        print("No books available in the library.")
    else:
        print("Books available in the library:")
        for book in self.books_list:
            print(f"- {book.book_name}, by {book.author_name} - {book.price}")
```

---

#### 2. Book Class

লাইব্রেরিতে একটি বইকে উপস্থাপন করার জন্য এই ক্লাসটি তৈরি করা হয়েছে। বইয়ের নাম, লেখকের নাম, এবং দাম সংরক্ষণ করে।
#### `Attributes`

    book_name: বইয়ের নাম।
    author_name: লেখকের নাম।
    price: বইয়ের দাম।
```python
class Book:
    def __init__(self, book_name, author_name, price):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price
```

---

#### Usage
#### 1. লাইব্রেরি অবজেক্ট তৈরি করুন।

```python
my_library = Library()
```

#### 2. বই তৈরি করুন।
```python
book_1 = Book("Python Programming", "John Doe", 500)
book_2 = Book("Java Programming", "Jane Doe", 600)
```

#### 3. লাইব্রেরিতে বই যোগ করুন।
```python
my_library.book_add(book_1)
my_library.book_add(book_2)
```


#### 4. লাইব্রেরির বইয়ের তালিকা দেখুন।
```python
my_library.book_list_show()
```


#### 5. বই মুছে ফেলুন।
```python
my_library.book_remove(book_1)
```

#### 6. তালিকা আবার দেখুন।

```python
my_library.book_list_show()
```


#### Sample Output
```plaintext
Python Programming, by John Doe - 500 has been added to the library.
Java Programming, by Jane Doe - 600 has been added to the library.

Books available in the library:
- Python Programming, by John Doe - 500
- Java Programming, by Jane Doe - 600

Python Programming has been removed from the library.

Books available in the library:
- Java Programming, by Jane Doe - 600
```
