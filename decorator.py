def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper
@decorator
def greet():
    print("Hello Ankit")
greet()

def decorator_name(func):
    def wrapper(*args,**kwargs):
        print("Before execution")
        result = func(*args,**kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a,b):
    return a+b
print(add(9,9))


# Function is an first class object

def calculate(*args):
    result = 0
    for _ in args:
        result = result + _
    return result

print(calculate(9,7))

def add_one(f,v):
    return f(v) + 1

final = add_one(calculate,5)
print(final)

# Returning a function from another function

def mul1(x):
    def mul2(y):
        return x*y
    return mul2

mul=  mul1(9)
print(mul(9))

def squre(x):
    return x*x

def num(f,x):
    return f(x)

print(num(squre,9))

# Decorators in methos

def method_decorator(func):
    def wrapper(self,name):
        print("Befor the execution")
        res = func(self,name)
        print("After the execution")
        return res
    return wrapper

class myclass:
    @method_decorator
    def greet(self,name):
        print(f"hello,{name}")
obj = myclass()
obj.greet("Ankit")
    
#Functions are objects — they can have attributes:
def counter():
    counter.count += 1
    return counter.count

counter.count = 0

print(counter())
print(counter())
print(counter())