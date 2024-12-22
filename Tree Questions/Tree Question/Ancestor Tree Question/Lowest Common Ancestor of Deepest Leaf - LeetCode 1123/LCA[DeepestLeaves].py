# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root
        
        left = self.height(root.left)
        right = self.height(root.right)

        if(left==right):
            return root
        elif left<right:
            return self.lcaDeepestLeaves(root.right)
        else:
            return self.lcaDeepestLeaves(root.left)

    def height(self,root):
        if root is None:
            return 0
        
        return 1+max(self.height(root.left),self.height(root.right))
        