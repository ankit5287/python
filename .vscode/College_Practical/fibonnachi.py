n = int(input("Enter the number of terms: "))
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
    sum = a+b
    a = b
    b = sum
    print(sum,end="\n")