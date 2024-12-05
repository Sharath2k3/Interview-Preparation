class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1
    
    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight,rheight) + 1

root = Node(2)
root.left = Node(1)
root.right = Node(3)
print(height(root))
    
    