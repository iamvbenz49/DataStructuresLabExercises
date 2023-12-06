class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
    def push(self,data):
        if not self.top:
            self.top = Node(data)
            return
        node = Node(data)
        node.next = self.top
        self.top = node
    def pop(self):
        if not self.top:
            return "Stack Underflow"
        node = self.top.data
        self.top = self.top.next
        return node
    def peek(self):
        if not self.top:
            return "Stack Underflow"
        node = self.top.data
        return node
    def display(self):
        temp = self.top
        print("|   |")
        while temp:
            print("| "+str(temp.data)+" |")
            temp = temp.next
        print("----- ")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.display()