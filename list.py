# List items are ordered, changeable, and allow duplicate values.

arr = [1, 2, 3, 4, 5]

# insert/delete
arr.pop()
arr.append(78)
arr.remove(3)
print(arr)

# Sorting

arr.sort()
rev = arr.sort(reverse = True) #decending order
print(arr)
print(rev)

# List comprehension
even = [val for val in arr if val%2==0]
print(even)

squre = [val**2 for val in range(1,9,2)]
print(squre)


