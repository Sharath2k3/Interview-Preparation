class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def levelorder_traversal(root):
    if root is None:
        return
    
    result = []
    queue = [root]
    
    while(len(queue)>0):
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.data)
            
            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)
            
        result.append(level)
        
    return result

root = Node(2)
root.left = Node(1)
root.right = Node(3)
print(levelorder_traversal(root))