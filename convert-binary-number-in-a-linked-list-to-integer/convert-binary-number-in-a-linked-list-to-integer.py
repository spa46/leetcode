# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def getval(head):
            if head:
                # print(head.val)
                index, sum = getval(head.next)
                sum = sum + (index * head.val)
                index = index*2
                return index, sum
                
            else:
                return 1,0
        _, sum = getval(head)
        
        # print(sum)
        return sum