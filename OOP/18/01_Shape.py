class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangel:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    # def perimeter(self):
    #     return 2 * (self.length + self.breadth)
    
class Square(Rectangel):
    def __init__(self, side):
        super().__init__(side, side)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    # def perimeter(self):
    #     return self.base + self.height + (self.base**2 + self.height**2)**0.5

# Function to show area of different shapes
def area_show(shape, *args):
    print(f"{shape.__class__.__name__}-Area: {shape.area(*args)}")


# Creating object of Circle class
c = Circle(5)
r = Rectangel(5, 12)
t1 = Triangle(5, 12)


area_show(c)
area_show(r)
area_show(t1)