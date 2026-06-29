def outer(x):
    def inner(y):
        return x+y
    return inner
closure = outer(2)

print(closure(9))

def multipler(x):
    def multiply_by(y):
        return x*y
    return multiply_by

c1 = multipler(6)
print(c1(7))

double = multipler(2)
print(c1(6))

print(double.__closure__[0].cell_contents)