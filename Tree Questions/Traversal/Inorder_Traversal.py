class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def inorder_traversal(root):
    if root is None:
        return 
    
    inorder_traversal(root.left)
    print(root.data,end=" ")
    inorder_traversal(root.right)

root = Node(2)
root.right = Node(3)
root.left = Node(1)
inorder_traversal(root)