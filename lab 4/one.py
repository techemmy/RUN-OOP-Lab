# Lab 4: Polymorphism and Method Overloading
"""
Method overloading is essentially a feature of object oriented languages,
in which we can have two or more methods functions that have the same name
but the parameters that they take as input values are different.

In this case, the `calculate_area` method of the Rectangle and Circle classes are perfect examples -
the same name, but different parameters. Rectangle takes in two paramters width and height while
Circle takes in just one, radius
"""

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def calculate_area(self, width, height):
        return width * height

class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius * radius

# Test the Shape, Rectangle, and Circle classes
rectangle = Rectangle()
rectangle_area = rectangle.calculate_area(5, 3)
print("Rectangle Area:", rectangle_area)
circle = Circle()
circle_area = circle.calculate_area(2)
print("Circle Area:", circle_area)
