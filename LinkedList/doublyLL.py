class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def _empty(self):
        return self.head == None
    def append(self,data):
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        node = Node(data)
        temp.next = node
        node.prev = temp
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="<->")
            temp = temp.next
        print()
    def prepend(self,data):
        if self._empty():
            self.head = Node(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def delete(self,data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        temp = self.head
        while temp.data != data:
            temp = temp.next
        if temp.next == None:
            temp.prev.next = None
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
LL = LinkedList()
LL.append(19)
LL.append(34)
LL.prepend(21)
LL.display()
LL.delete(19)
LL.delete(34)
LL.display()