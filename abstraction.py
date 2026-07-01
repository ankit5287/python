#Use Abstraction to keep your code clean, organized, and professional.

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass




class Dog(Animal):
    
    def makeSound(self): #Can't instantiate abstract class Dog without an implementation for abstract method 'makeSound' in abstraction
        return "barking"
    def move(self):
        return "moving"
    
dog = Dog()
print(dog.move())
print(dog.makeSound())

# Example

from abc import ABC, abstractmethod

class Shape(ABC):                    # Abstract class
    
    @abstractmethod
    def area(self):                  # Must be implemented by subclasses
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):                  # Required implementation
        return self.w * self.h
    
    def perimeter(self):             # Required implementation
        return 2 * (self.w + self.h)

# s = Shape()        # ❌ Can't instantiate abstract class
r = Rectangle(5, 3)  # ✅ Works


