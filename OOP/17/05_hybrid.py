class Base:
    def base_method(self):
        print("This is the base class")

class Child1(Base):
    def child1_method(self):
        print("This is the first Child class")

class Child2(Base):
    def child2_method(self):
        print("This is the second Child class")

class GrandChild(Child1, Child2):
    def grandchild_method(self):
        print("This is the GrandChild class")

# create object of GrandChild class
obj = GrandChild()
obj.base_method()  # Base class method
obj.child1_method()  # Child1 class method
obj.child2_method()  # Child2 class method 
obj.grandchild_method()  # GrandChild class method