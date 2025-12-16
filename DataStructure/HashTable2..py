class HashTable():
    def __init__(self,size):
        self.size = size
        self.table = [[None]]*10

    def hash_function(self,name):
        char_sum = 0
        for char in name:
            char_sum += ord(char)
        return char_sum%10
    
    def add(self,name):
        index = self.hash_function(name)
        self.table[index] = name

    def contain(self, name):
        index = self.hash_function(name)
        return self.table[index] == name
    
    def search(self,name):
        index = self.hash_function(name)
        return name in self.table[index]
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

n1 = HashTable(3)
n1.add("bob")
n1.add("Jim")
n1.add("Mike")

n1.display()

print(n1.contain("bob"))
