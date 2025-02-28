import sys

class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")  # Dog object is created
print(sys.getrefcount(dog1))  # Reference count (usually 2, one from sys.getrefcount itself)

dog2 = dog1  # Another reference to the same object
print(sys.getrefcount(dog1))  # Reference count increases

del dog1  # Remove one reference
print(sys.getrefcount(dog2))  # Reference count decreases

del dog2  # No references left → Memory is freed automatically
