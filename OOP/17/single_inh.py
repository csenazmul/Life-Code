# Single Inheritance

class Parent:
    def display(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        print("This is the child class.")

# Creating object of child class
c = Child()
c.display() # Parent class method
c.show() # Child class method


class পিতা:
    def বৈশিষ্ট্য(self):
        print("আমি পরিবারের অভিভাবক ।")

class সন্তান(পিতা):
    def ভূমিকা(self):
        print("আমি পরিবারের একজন সদস্য ।")

স = সন্তান()
স.বৈশিষ্ট্য() # পিতা ক্লাসের মেথড
স.ভূমিকা() # সন্তান ক্লাসের মেথড



class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
    
    def login(self):
        print(f"{self.name} has logged in.")

class Employee(User):
    def __init__(self, user_id, name, department):
        super().__init__(user_id, name) # super() function
        self.department = department

    def work(self):
        print(f"{self.name} is working in {self.department} department.")

# Creating object of Employee class
employee = Employee(101, "John Doe", "IT")
employee.login() # User class method
employee.work() # Employee class method