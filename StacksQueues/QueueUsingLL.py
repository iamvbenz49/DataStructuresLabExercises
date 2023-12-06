class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    def enqueue(self,data):
        if not self.front:
            self.front = self.rear = Node(data)
            return
        node = Node(data)
        self.rear.next = node
        self.rear = node
    def dequeue(self):
        if not self.front:
            return "Queue Empty"
        node = self.front.data
        self.front = self.front.next
        return node
    def display(self):
        temp = self.front
        print("Front",end="<->")
        while temp:
            print(str(temp.data),end="<->")
            temp = temp.next
        print("Rear")
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.display()