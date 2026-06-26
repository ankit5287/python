# Arithmatic oprator
a = 15
b = 4

print("Addition:", a + b)  

print("Subtraction:", a - b) 

print("Multiplication:", a * b)  

print("Division:", a / b) 

print("Floor Division:", a // b)  

print("Modulus:", a % b) 

print("Exponentiation:", a ** b)

# Comparision Oprator

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Bitwise Oprator

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# Assignment Oprator

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

x = 24
y = 20

my_list = [10, 20, 30, 40, 50]



if (x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in my_list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# loical oprator

a = True
b = False
print(a and b)
print(a or b)
print(not a)

# Identitty Oprator

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# membership oprator

l = [1, 2, 3, 4, 5]
s = "Hello World"
d = {1: "Geeks", 2: "for", 3: "geeks"}

print(2 in l)
print('O' in s)
print(3 in d)