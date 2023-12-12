class heap:
    def __init__(self) -> None:
        self.hp = []
        self.size = 0
    def parent(self,node):
        return node//2
    def left(self,node):
        return 2*node + 1
    def right(self,node):
        return 2*node + 2
    def insert(self,val):
        self.hp.append(val)
        self.size+=1
        self.upheap(self.size-1)
    def upheap(self,index):
        if index==0:
            return 
        parent = self.parent(index)
        if self.hp[parent]<self.hp[index]:
            self.swap(parent,index)
            self.upheap(parent)
    def pop(self):
        ele = self.hp[0]
        self.hp[0] = self.hp[self.size-1]
        self.hp.pop()
        self.size-=1
        self.downheap(0)
        return ele 
    def downheap(self,index):
        left = self.left(index)
        right = self.right(index)
        min = index
        if left<self.size and self.hp[left]>self.hp[min]:
            min = left
        if right<self.size and self.hp[right]>self.hp[min]:
            min = right
        if min!=index:
            self.swap(min,index)
            self.downheap(min)
    def swap(self,i,j):
        self.hp[i],self.hp[j] = self.hp[j],self.hp[i]

hp = heap()
hp.insert(10)
hp.insert(20)
hp.insert(5)
print(hp.pop())
hp.insert(-1)
hp.insert(7)
hp.insert(-211)
print(hp.hp)
print(hp.pop())
print(hp.pop())
print(hp.hp)
print(hp.pop())
print(hp.pop())
print(hp.pop())