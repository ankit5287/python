a = int(input("Enter the firstNum:"))
b = int(input("Enter the secondNum:"))
c = int(input("Enter the thirdNum:"))

l1 = list()
l1.append(a)
l1.append(b)
l1.append(c)
n = len(l1)
for i in range(n):
    print("*"*l1[i])
