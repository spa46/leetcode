"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return root
        
        q = [root]
        qq = []
                
        while q:
            n = q.pop(0)
            if n.left:
                qq.append(n.left)
            if n.right:
                qq.append(n.right)
            
            if not q:
                if qq:
                    n = qq[0]
                    
                    for nn in qq[1:]:
                        n.next = nn
                        n = nn
                    
                q = qq
                
                qq = []
                
                
            
        
        return root