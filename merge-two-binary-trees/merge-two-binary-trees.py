# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    root3 = TreeNode()
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 and root2:
            ans = TreeNode(root1.val+root2.val)
            ans.left = self.mergeTrees(root1.left, root2.left)
            ans.right = self.mergeTrees(root1.right, root2.right)
            
            return ans
        else:
            return root1 or root2