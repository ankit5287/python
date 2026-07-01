#Use Abstraction to keep your code clean, organized, and professional.



class Animal():
    
    def makeSound(self):
        pass




class Dog(Animal):
    
    def makeSound(self):
        return "barking"
    def move(self):
        return "moving"
    
dog = Dog()
print(dog.move())
print(dog.makeSound())


class Cat(Animal):
    # Oops, forgot to implement makeSound!
    def purr(self):
        return "purring"

cat = Cat()
print(cat.makeSound())  