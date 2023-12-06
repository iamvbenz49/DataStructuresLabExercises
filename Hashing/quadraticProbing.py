class HashTable:
    def __init__(self,size) -> None:
        self.size = size
        self.table = [None]*size

    def _hash(self,key):
        return hash(key)%self.size
    
    def put(self,key,value):
        index = self._hash(key)
        step = 1
        while self.table[index]!=None and self.table[index]!="DEL":
            index = (index+(step*step))%self.size
        self.table[index] = (key,value)
    def get(self,key):
        index = self._hash(key)
        step = 1
        while self.table[index]:
            if self.table[index] !="DEL" and self.table[index][0] == key:
                return self.table[index][1]
            index = (index+(step*step))%self.size
        return
    def remove(self,key):
        index = self._hash(key)
        step = 1
        while self.table[index]:
            if self.table[index] !="DEL" and self.table[index][0] == key:
                self.table[index] = "DEL"
                return
            index = (index+(step*step))%self.size
    def display(self):
        for content in self.table:
            if content == "DEL" or content == None:
                print("None --> None")
            else:
                print(content[0],"-->",content[1])
tb = HashTable(10)
tb.put("vijay","benz")
tb.put("KL","Rahul")
tb.put("preyjvi","shaw")
tb.put("Virat","Kolhi")
tb.put("Chris","Evans")
tb.put("Loki","Odinson")
print(tb.get("KL"))
print(tb.get("vijayd"))
tb.display()
tb.remove("KL")
