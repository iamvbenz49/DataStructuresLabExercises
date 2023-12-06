class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    def insert(self,data):
        self.root = self._insert(self.root,data)
    def _insert(self,root,data):
        if not root:
            return Node(data)
        if root.data>data:
            root.left = self._insert(root.left,data)
        elif root.data<data:
            root.right = self._insert(root.right,data)
        return root
    def search(self,data):
        return self._search(self.root,data)
    def _search(self,root,data):
        if root.data == data:
            return root
        if root.data>data:
            root.left = self._search(root.left,data)
        elif root.data<data:
            root.right = self.search(root.right,data)
    def inorder(self):
        self._inorder(self.root)
    def _inorder(self,root):
        if root:
            self._inorder(root.left)
            print(root.data,end=' ')
            self._inorder(root.right)
        else:
            print("n")
tree = BST()
for i in range(10):
    tree.insert(i)
tree.inorder()