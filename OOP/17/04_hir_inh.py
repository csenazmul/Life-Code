# Description: Hierarchical Inheritance in Python
class Parent:
    def parent_method(self):
        print("This is the parent class.")

class Child1(Parent):
    def child1_method(self):
        print("This is the first child class.")

class Child2(Parent):
    def child2_method(self):
        print("This is the second child class.")

# উদাহরণ:
obj1 = Child1()
obj2 = Child2()

obj1.parent_method()  # Parent class method (Child1 instance)
obj1.child1_method()  # Child1 specific method

obj2.parent_method()  # Parent class method (Child2 instance)
obj2.child2_method()  # Child2 specific method
