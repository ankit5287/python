class Stack:
    def __init__(self, size):
        self.size = size
        self.l = []

    def add(self, element):
        if len(self.l) < self.size:
            self.l.append(element)
        else:
            print("Stack is full")

    def peek(self):
        if len(self.l) == 0:
            print("Stack is empty")
        else:
            print(self.l[-1])
    
    def display(self):
        print(self.l)

    def pop(self):
        if len(self.l) == 0:
            print("Stack is empty")
        else:
            return self.l.pop()

s1 = Stack(5)

s1.add(90)
s1.add(45)
s1.add(78)
s1.add(12)
s1.display()
s1.pop()
s1.display()
s1.peek()