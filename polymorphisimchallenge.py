class Animal:
    def move(self):
        pass  # Abstract method placeholder

class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🦅")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

# Using polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
