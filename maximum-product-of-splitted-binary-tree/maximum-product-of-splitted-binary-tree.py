from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = defaultdict(TreeNode)
        
        def dfs(root):
            if root:
                a = dfs(root.left)
                b = dfs(root.right)
                d[a+b+root.val] = True
                # print(a+b+root.val)
                return a+b+root.val
            else:
                return 0
        t = dfs(root)

        m=0
        for k in d.keys():
            m = max(m, (t-k)*k)
            
        return m % 1000000007
        