def greet(name):
    return f"Hello {name}"

name1 = greet("Ankit")

# print(name1)

fun = [greet,len,name1]
print(fun[0]("Ankit"))

# global and non global keyword

count = 0

def sum():
    global count
    count += 1
    return count

sum()
print(count)

def outer():
    s1 = outer
    def inner():
        nonlocal s1
        s1 = "inner"
    
    inner()
    print(s1)

outer()

# Default Argument - Evalucated once when function is called
# Same list
def add_value(item,items = []):
    items.append(item)
    return items

#Diffrent list every time

print(add_value(9))
print(add_value(3))
print(add_value(4))
print(add_value(5))

def add_item(item,items = None):
    if items == None:
        items = []
    items.append(item)
    return items

print(add_item(1))
print(add_item(6))
print(add_item(3))

# **args and **kwrgs

def arg_sum(*args):
    result = 0
    for num in args:
        result += num
    return result

print(arg_sum(1,2,3,6))

nums = [3,4,5]
arg_sum(*nums)
def greet(name):
    return f"Hello {name}"

name1 = greet("Ankit")

# print(name1)

fun = [greet,len,name1]
print(fun[0]("Ankit"))

# global and non global keyword

count = 0

def sum():
    global count
    count += 1
    return count

sum()
print(count)

def outer():
    s1 = outer
    def inner():
        nonlocal s1
        s1 = "inner"
    
    inner()
    print(s1)

outer()

# Default Argument - Evalucated once when function is called
# Same list
def add_value(item,items = []):
    items.append(item)
    return items

#Diffrent list every time

print(add_value(9))
print(add_value(3))
print(add_value(4))
print(add_value(5))

def add_item(item,items = None):
    if items == None:
        items = []
    items.append(item)
    return items

print(add_item(1))
print(add_item(6))
print(add_item(3))

# **args and **kwrgs

def arg_sum(*args):
    result = 0
    for num in args:
        result += num
    return result

print(arg_sum(1,2,3,6))

nums = [3,4,8]
print(arg_sum(*nums))


def info(**kwargs):
    print(kwargs)

data = {
    "name" : "Ankit",
    "Marks" : 90
}

info(**data)

#Lambda Function

def squre(*args,items = []):
    for _ in args:
        items.append(_**2)
    return items

num = [1,2,3,7,8]
print(squre(*num))

s = lambda x : x**2
print(s(9))

students = [("Ankit",90),("Gaurav",78)]

students.sort(key=lambda x : x[1])
print(students)

