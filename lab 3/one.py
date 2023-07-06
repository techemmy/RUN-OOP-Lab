# Encapsulation and Abstraction

class Employee:
    def __init__(self):
        self.__name = None
        self.__salary = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

john = Employee()
john.set_name("John")
john.set_salary(50000)
print(john.get_name(), john.get_salary()) # output: John 50000
