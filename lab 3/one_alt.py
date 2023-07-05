# Alternative solution to solution 1
class Employee:
    def __init__(self):
        self.__name = None
        self.__salary = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

james = Employee()
james.name = "James"
james.salary = 100000
print(james.name, james.salary) # output: James 100000

john = Employee()
john.__name = "John"
john.__salary = 60000
# the print statement should return "None None"
# because __name & __salary shouldn't be assessed directly (Abstraction)
print(john.name, john.salary) # output: None None
