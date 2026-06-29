squre = [x**2 for x in range(100000)] #Use so much memory

squre = (x**2 for x in range(12,20))
print("Squre of an 8 numbers using na genrator")
for _ in range(8):
    print(next(squre))

a = [1,2,3]
b = [1,2,3]

print(a is b) #diffrent object in memory
print(a==b) #check value

