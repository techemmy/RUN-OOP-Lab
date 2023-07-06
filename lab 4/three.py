# Lab 4: Polymorphism and Method Overloading

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def calculate_area(self, width, height):
        return width * height

class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius * radius


class Calculator:
    def add(self, num1, num2):
        if type(num1) is str and type(num2) is str:
            return num1 + num2
        elif type(num1) is int and type(num2) is int:
            return int(num1) + int(num2)


# Test the Shape, Rectangle, and Circle classes
rectangle = Rectangle()
rectangle_area = rectangle.calculate_area(5, 3)
print("Rectangle Area:", rectangle_area) # output: Rectangle Area: 15

circle = Circle()
circle_area = circle.calculate_area(2)
print("Circle Area:", circle_area) # output: Circle Area: 12.56

calc = Calculator()
strings_sum = calc.add("10", "20")
print(strings_sum) # output: "1020"
numbers_sum = calc.add(10, 20)
print(numbers_sum) # output: 30
