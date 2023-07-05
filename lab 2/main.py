# Inheritance and Polymorphism
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}, Breed: {self.breed}"

animal = Animal("Max", 5)
print(animal)
dog = Dog("Buddy", 3, "Labrador")
print(dog)
