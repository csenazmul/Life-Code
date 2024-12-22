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


#### `book_add(book_name)`
নতুন বই লাইব্রেরিতে যোগ করার জন্য ব্যবহৃত হয়।
```python
def book_add(self, book_name):
    self.books_list.append(book_name)
    print(f"{book_name} has been added to the library.")
