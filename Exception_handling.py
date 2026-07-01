#Python provides four main keywords for handling exceptions:
#try, except, else and finally each plays
#a unique role. Let's see syntax:

n = 10
try:
    x =n/0
except ZeroDivisionError:
    print("can not devide by zero")

else:
    print(f"result is:{x}")

# will executed wheather their is an error or not
finally:
    print("execution completed")

#Errors vs Exceptions
#Errors and exceptions are both issues in a program, but they differ in severity and handling.

#Error: Issues in the program logic such as SyntaxError, etc. It occurs at compile time.
#Exception: Problems that occur at runtime and can be managed using exception handling
# (e.g., invalid input, missing files).