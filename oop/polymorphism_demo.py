
class Shape:
    
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        return f"{rectangle_area}"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        circle_area = math.pi * self.radius ** 2
        return f"{circle_area}"