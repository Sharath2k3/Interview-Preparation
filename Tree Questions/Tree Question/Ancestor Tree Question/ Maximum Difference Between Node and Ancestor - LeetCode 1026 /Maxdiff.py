
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        self.diff = 0
        self.helper(root,root.val,root.val)
        return self.diff

    def helper(self,root,min_val,max_val):
        if root is None:
            return 0
        self.diff = max(self.diff , max(abs(min_val-root.val),abs(max_val-root.val)))
        min_val = min(min_val,root.val)
        max_val = max(max_val,root.val)
        self.helper(root.left,min_val,max_val)
        self.helper(root.right,min_val,max_val)