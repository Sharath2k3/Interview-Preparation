class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postorder_traversal(root):
    if root is None:
        return 
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data,end="")

root = Node(2)
root.left = Node(1)
root.right = Node(3)
postorder_traversal(root)