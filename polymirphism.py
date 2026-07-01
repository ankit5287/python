#Polymorphism — Same interface, different behaviors

class animal:
    def speak(self):
        pass

class dog(animal):
    def speak(self):
        return "woof"
    
class cat(animal):
    def speak(self):
        return "meow"
    
class cow(animal):
    def speak(self):
        return "moo"
    
animals = [dog(),cat(),cow()]

for animal in animals:
    print(animal.speak())
    