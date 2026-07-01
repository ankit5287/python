class Animal:
    def __init__(self,name):
        self.name = name
        pass

    def speck(self):
        raise NotImplementedError("Must be implement in subclass")
    
    def introduce(self):
        return f"my name is:{self.name}"
    
class Dog(Animal):
    def speck(self):
        return "woof"

dog = Dog("Buddy")
print(dog.speck())        
print(dog.introduce())        

