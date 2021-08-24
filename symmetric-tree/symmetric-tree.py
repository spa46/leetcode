# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(a, b):
            if a and b:
                v1 = dfs(a.left, b.right)
                v2 = dfs(a.right, b.left)
                
                if not v1 or not v2:
                    return False
                
                if a.val != b.val:
                    return False
                
                return True
            elif not a and not b:
                return True
            else:
                return False
            
        
    
        return dfs(root.left, root.right)
        