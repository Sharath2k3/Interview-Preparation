# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def postorder(root):
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)
        
        postorder(root)
        return result