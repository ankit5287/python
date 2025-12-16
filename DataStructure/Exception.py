try:
    print(x)
except:
    print("Exception Occured")

try:
    x1 = 90
    print(x1)
except:
    print("Exception Occured")

#Else block will execute if no error occur

try:
    x2 = 78
    print(x2)
except:
    print("Something went wrong")
else:
    print("Nothing is wrong")

try:
    print(x3)
except:
    print("can't find value")
else:
    print("Nothing is wrong")

# Finally bock will execute,
# regardless there is an error occur or not if specified

try:
    print(x3)
except:
    print("can't find value of x3")
finally:
    print("This is the end of the program and it willexcute wheather there is an error or not")

try:
    x3 = 45
    print(x3)
except:
    print("can't find value of x3")
finally:
    print("This is the end of the program and it willexcute wheather there is an error or not")

# Raise

num = "Hello"

if not type(num) is int:
    print("Only integer are allowed")

def jls_extract_def():
    c = -1
    
    if c<0:
        raise Exception("no number less thenn 0")
    return c

c = jls_extract_def()