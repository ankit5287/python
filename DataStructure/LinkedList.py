class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(2)
n2 = Node(3)
n3 = Node(7)

n1.next = n2
n2.next = n3

cNode = n1
while cNode:
    print(cNode.data,end="->")
    cNode = cNode.next
print("Null")

