# Encapsulation and Abstraction

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius**2)

rect_1 = Rectangle(50, 20)
print("Rectangle area:", rect_1.calculate_area())

circle = Circle(10)
print("Circle area:", circle.calculate_area())
