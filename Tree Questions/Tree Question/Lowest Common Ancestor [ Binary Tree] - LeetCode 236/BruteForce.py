# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestors_of_p = []
        ancestors_of_q = []

        self.ancestor(root,p,ancestors_of_p)
        self.ancestor(root,q,ancestors_of_q)

        lca = None
        for a,b in zip(ancestors_of_p[::-1],ancestors_of_q[::-1]):
            if a==b:
                lca = a
            else:
                break
        
        return lca

    def ancestor(self,root,target,result):
        if root is None:
            return False
            
        if root == target:
            result.append(root)
            return True
            
        if self.ancestor(root.left,target,result) or self.ancestor(root.right,target,result):
            result.append(root)
            return True
            
        return False