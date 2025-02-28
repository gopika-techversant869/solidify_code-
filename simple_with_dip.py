"""
------------------Dependency Inversion Principle (DIP)------------------------------

Here first we create the reference of the dog to the AnimalSpeaker class, 
-> AnimalSpeaker does not decide which animal to use.
-> Instead, it accepts any object that follows IAnimal (either Dog or Cat).
-> It then calls self.animal.speak(), without worrying about which animal it is.

"""
from abc import ABC, abstractmethod

# 1. Define an interface
class IAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(IAnimal):
    def speak(self):
        return "Woof!"

class Cat(IAnimal):
    def speak(self):
        return "Meow!"

class AnimalSpeaker:
    def __init__(self, animal: IAnimal):
        self.animal = animal

    def make_sound(self):
        return self.animal.speak()
    
dog_speaker = AnimalSpeaker(Dog())  
print(dog_speaker.make_sound())  

cat_speaker = AnimalSpeaker(Cat())  
print(cat_speaker.make_sound()) 

dog_speaker = AnimalSpeaker(Dog())  
print(dog_speaker.make_sound()) 


"""
How memory works here?

-> Dog and Cat are created outside, so they can be reused.
-> AnimalSpeaker only holds a reference to an existing object.
-> No extra objects are created unnecessarily.
-> Even if we create the another dog objects here reuse the dog objects we created at earlier

DIP prevents unnecessary object creation, reducing memory usage and improving performance!

"""