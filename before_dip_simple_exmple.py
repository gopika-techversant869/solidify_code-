
"""
-> AnimalSpeaker decides which animal to use → Hard to change later.
-> If a new animal (example:Bird) is added, we must modify AnimalSpeaker.

"""



class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalSpeaker:
    def __init__(self, animal_type):
        if animal_type == "dog":
            self.animal = Dog()  # Directly creating Dog instance
        elif animal_type == "cat":
            self.animal = Cat()  # Directly creating Cat instance
        else:
            raise ValueError("Unknown animal type")

    def make_sound(self):
        return self.animal.speak()

speaker = AnimalSpeaker("dog")
print(speaker.make_sound()) 
speaker = AnimalSpeaker("cat")
print(speaker.make_sound())
