# Introduction to Classes and Objects

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print("Area:", rect.calculate_area()) # output: Area: 15
print("Perimeter:", rect.calculate_perimeter()) # output: Perimeter: 16
