import pytest
import shapes
import math

# class TestRectangle:
#     def setup_rec(self):
#         self.rec = shapes.Rectangle(10,20)
        
#     def test_area(self):
#         assert self.rec.area == self.rec.length * self.rec.width
        
#     def test_perimeter(self):
#         assert self.rec.perimeter == 2 * (self.rec.length + self.rec.width)

def test_area(my_rec):
    assert my_rec.area() == my_rec.length * my_rec.width
    
def test_perimeter(my_rec):
    assert my_rec.perimeter() == 2 * (my_rec.length + my_rec.width)
    
def test_not_equal(my_rec,weird_rectangle):
    assert my_rec!= weird_rectangle
    
