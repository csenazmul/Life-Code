# Multiple Inheritance

class Father:
    def father_method(self):
        print("This is the father class.")

class Mother:
    def mother_method(self):
        print("This is the mother class.")

class Child(Father, Mother):
    def child_method(self):
        print("This is the child class.")

# Creating object of child class
c = Child()
c.father_method() # Father class method
c.mother_method() # Mother class method
c.child_method() # Child class method