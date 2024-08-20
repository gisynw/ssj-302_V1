# code in shapes.py
import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius**2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self,length,width) -> None:
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Rectangle):
            return False
        return self.width == other.width and self.length == self.length
    
class Square(Rectangle):
    def __init__(self, side_length) -> None:
        super().__init__(side_length, side_length)