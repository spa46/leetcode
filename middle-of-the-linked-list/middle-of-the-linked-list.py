# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def traverse(n):
            if not n:
                return 0
            else:
                return traverse(n.next) + 1
        
        total = traverse(head)
        mid = total / 2
        # print(mid)
        
        for i in range(mid):
            head = head.next
        
        return head