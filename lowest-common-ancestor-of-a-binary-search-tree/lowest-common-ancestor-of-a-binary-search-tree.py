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
        
        if root:
            a = self.lowestCommonAncestor(root.left, p, q)
            b = self.lowestCommonAncestor(root.right, p, q)

            if root.val == p.val or root.val == q.val:
                return root
            
            if a and not b:
                return a
            elif not a and b:
                return b
            elif a and b:
                return root
            else: 
                return None
        else:
            return None
        
        