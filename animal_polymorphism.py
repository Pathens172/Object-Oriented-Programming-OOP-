# A base class for an Animal
class Animal:
    def move(self):
        return "This animal moves in some way."

# A Dog class that inherits from Animal
class Dog(Animal):
    def move(self):
        return "The dog runs 🐕."

# A Bird class that inherits from Animal
class Bird(Animal):
    def move(self):
        return "The bird flies 🐦."

# A Fish class that inherits from Animal
class Fish(Animal):
    def move(self):
        return "The fish swims 🐟."

# Create objects for each class
dog = Dog()
bird = Bird()
fish = Fish()

# Call the move() method for each object
animals = [dog, bird, fish]

for animal in animals:
    print(animal.move())
