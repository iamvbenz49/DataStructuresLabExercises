class Queue:
    def __init__(self) -> None:
        self._enqueue = []
        self._dequeue = []
    
    def _empty(self):
        return not self._enqueue or self._dequeue
    
    def enqueue(self,data):
        self._enqueue.append(data)
    
    def dequeue(self):
        if not self._dequeue:
            if not self._enqueue:
                return "Queue Empty"
            while self._enqueue:
                self._dequeue.append(self._enqueue.pop())
        return self._dequeue.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

