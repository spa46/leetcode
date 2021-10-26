# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(root):
            if not root:
                return None
            
            if root.left and root.right:
                tmp = root.left
                root.left = root.right
                root.right = tmp
            elif root.left:
                root.right = root.left
                root.left = None
            elif root.right:
                root.left = root.right
                root.right = None
            else:
                return None

            self.invertTree(root.left)
            self.invertTree(root.right)
        
            return None
        
        dfs(root)
        return root