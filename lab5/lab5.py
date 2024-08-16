class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        return "I am eating"


class Cat(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight)
        self.age = age

    def eat(self):
        return "I am eating fish"

    def meow(self):
        return "I meow when I'm hungry"
