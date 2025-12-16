class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

n1 = Node(4)
n2 = Node(9)
n3 = Node(2)

n1.next = n2
n2.next = n3

n1.pre = None
n2.pre = n1
n3.pre = n2
# Forword Traversal
cNode = n1
while cNode:
    print(cNode.data,end="->")
    cNode = cNode.next
print("Null")

# Backword Traversal

cNode = n3
while cNode:
    print(cNode.data,end="->")
    cNode = cNode.pre
print("Null")

