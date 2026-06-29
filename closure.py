def outer(x):
    def inner(y):
        return x+y
    return inner
closure = outer(2)

print(closure(9))