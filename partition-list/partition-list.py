# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        lx = None
        ly = None
        lx_curr = None
        ly_curr = None
        
        
        while head:            
            if head.val < x:
                if lx_curr:
                    lx_curr.next = ListNode(head.val)
                    lx_curr = lx_curr.next
                else:
                    lx_curr = ListNode(head.val)
                    lx = lx_curr
            else:
                if ly_curr:
                    ly_curr.next = ListNode(head.val)
                    ly_curr = ly_curr.next
                else:
                    ly_curr = ListNode(head.val)
                    ly = ly_curr
            head = head.next
        
        if not lx:
            return ly
        elif not ly:
            return lx
        else:
            lx_curr.next = ly
            return lx
        