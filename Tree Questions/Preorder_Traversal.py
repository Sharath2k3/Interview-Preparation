class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is None:
        return
    
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

root = Node(2)
root.left = Node(1)
root.right = Node(3)
preorder_traversal(root)