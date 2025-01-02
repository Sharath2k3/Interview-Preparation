# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0
        def height(root):
            if root is None:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)
            self.diameter = max(self.diameter,lheight+rheight)

            return 1+max(lheight,rheight)
        height(root)
        return self.diameter