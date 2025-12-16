def HashTable(name):
    char_sum = 0
    for char in name:
        char_sum += ord(char)
    return char_sum%10

print(HashTable("Ankit"))
l1 = [None]*10
def add(name):
    index = HashTable(name)
    l1[index] = name

add("Ankit")
print(l1)

add("Prince")
add("Ravi")

print(l1)

def contain(name):
    index = HashTable(name)
    return l1[index] == name

print(contain("Ankit"))
print(contain("Parv"))
