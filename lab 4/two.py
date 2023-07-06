# Lab 4: Polymorphism and Method Overloading

class Calculator:
    def add(self, num1, num2):
        if type(num1) is str and type(num2) is str:
            return num1 + num2
        elif type(num1) is int and type(num2) is int:
            return int(num1) + int(num2)
