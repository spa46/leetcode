# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        def dfs(root, n):
            if root:
                l = dfs(root.left, n)
                r = dfs(root.right, n)
                
                if l or r:
                    return l or r
                    

                if k-root.val in n:
                    return True
                
                n.add(root.val)
                
                
                return False
                
        return dfs(root, set())