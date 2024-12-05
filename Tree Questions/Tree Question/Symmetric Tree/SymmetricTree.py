# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isMirror(self,left,right):
        #Both of the Tree is None , both Trees are Symmetric
        if left is None and right is None:
            return True
        #If one of the either trees are null , then they are not symmetric 
        if left is None or right is None:
            return False
        #Since Symmetry - Compare [left.left and right.right and left.right and right.left]
        return left.val==right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left,root.right)
            