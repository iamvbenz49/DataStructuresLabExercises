class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.right = Node(4)
root.left.left = Node(2)
root.right.right = Node(8)
root.right.left = Node(6)
inorder(root)
print()
preorder(root)
print()
postorder(root)

