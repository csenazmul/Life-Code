# Multilevel Inheritance in Python
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent class.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent class.")

class Child(Parent):
    def child_method(self):
        print("This is the child class.")

# Creating object of child class
c = Child()
c.grandparent_method()  # Grandparent class method
c.parent_method()       # Parent class method
c.child_method()        # Child class method
