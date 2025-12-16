# class Person():
#     def __init__(self,email,age = 90):
#         self.email = email
#         self.age = age

# first = Person("ankitnandoliya32@gmail.com")
# print(first.email)
# print(first.age)

# class person2():
#     pass

# p1 = person2()
# p1.name = "Ankit"
# p1.age = 90

# print(p1.name)
# print(p1.age)

class Person():
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print("Hello " + self.name)

    def welcome(self):
        print(self.name + ",Welcome to our website")

p1 = Person("Ankit")
p1.greet()
p1.welcome()

class Car():
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def specification(self):
        print(f"This is an {self.model} ,made in year {self.year}")
c1 = Car("Fortuner",2023)
print(c1.model)
print(c1.year)
print(c1.specification())