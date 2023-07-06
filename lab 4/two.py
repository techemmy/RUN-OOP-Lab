# Lab 4: Polymorphism and Method Overloading

class Calculator:
    def add(self, num1, num2):
        if type(num1) == str and type(num2) == str:
            return num1 + num2
        elif type(num1) == int and type(num2) == int:
            return int(num1) + int(num2)
