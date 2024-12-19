# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathsum(self,root,target,sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            sum+=root.val
            if sum == target:
                return True
        return self.pathsum(root.left,target,sum+root.val) or self.pathsum(root.right,target,sum+root.val)
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        sum = 0
        return self.pathsum(root,targetSum,sum)
        