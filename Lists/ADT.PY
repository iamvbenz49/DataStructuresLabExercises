class ListADT:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 10
        self._arr = [None]*10
    def display(self):
        print("[",end=" ")
        for i in (range(self.size)):
            print(self._arr[i],end=" ")
        print("]")
    def size(self):
        return self.size==0
    def append(self,data):
        if self.capacity == self.size:
            self._resize()
        self._arr[self.size] = data
        self.size+=1
    def get(self,index):
        if 0<=index<self.size:
            return self._arr[index]
        raise IndexError("Index out Of Bound")
    def set(self,index,val):
        if 0<=index<self.size:
            self._arr[index] = val
            return 
        raise IndexError("Index out Of Bound")
    def _resize(self):
        self.capacity*=2
        temp = [None]*self.capacity
        for i in range(self.size):
            temp[i] = self._arr[i]
        self._arr = temp
    def index(self,val):
        for i in range(self.capacity):
            if self._arr[i]==val:
                return i
        return -1
    def remove_at(self,index):
        if 0<=index<self.size:
            for i in range(index,self.size-1):
                self._arr[i] = self._arr[i+1]
            self.size-=1
            return 
        raise IndexError("Index out Of Bound")
    def remove(self,data):
        index = self.index(data)
        self.remove_at(index)

list = ListADT()

while 1:
    option = """    MENU 
    1.Append Value
    2.Set Value
    3.Remove
    4.Display
    5.Exit"""
    print(option)
    n = int(input("Enter your choice : "))
    if n==1:
        list.append(int(input("enter the number : ")))
    elif n==2:
        list.set(int(input("enter the index :")),int(input("Enter the value : ")))
    elif n==3:
        list.remove(int(input("Enter the value to remove : ")))
    elif n==4:
        list.display()
    elif n==5:
        break
    else:
        print("Enter valid Choice ")

    