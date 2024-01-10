class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

    def wag_tail(self):
        return "{} is wagging its tail.".format(self.name)

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow! Meow!"

    def purr(self):
        return "{} is purring.".format(self.name)

# Example usage:
dog1 = Dog(name="Rocky", age=3, breed="Golden Retriever")
cat1 = Cat(name="Pursey", age=2, color="Tabby")

print("{} says: {}".format(dog1.name, dog1.make_sound()))
print("{} is {} years old.".format(dog1.name, dog1.age))
print(dog1.wag_tail())

print("{} says: {}".format(cat1.name, cat1.make_sound()))
print("{} is {} years old.".format(cat1.name, cat1.age))
print(cat1.purr())