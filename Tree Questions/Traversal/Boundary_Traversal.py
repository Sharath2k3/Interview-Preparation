class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def leftboundary(root):
    if not root:
        return 
    while root:
        if root.left or root.right:
            print(root.data,end=" ")
        if root.left:
            root = root.left
        else:
            root = root.right

def rightboundary(root):
    if not root:
        return 
    stack = []
    while root:
        if root.left or root.right:
            stack.append(root.data)
        if root.right:
            root = root.right
        else:
            root = root.left
    while stack:
        print(stack.pop(),end=' ')

def printleaves(root):
    if root is None:
        return
    printleaves(root.left)
    if not root.left and not root.right:
        print(root.data,end = " ")
    printleaves(root.right)

def boundary(root):
    print(root.data,end = " ")
    leftboundary(root.left)
    printleaves(root.left)
    printleaves(root.right)
    rightboundary(root.right)

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)

boundary(root)