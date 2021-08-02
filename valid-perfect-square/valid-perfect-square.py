class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num == 1:
            return True
        
        left = 0
        right = num
        
        while left<right:
            mid = (left+right)/2
            
            if mid**2 > num:
                right = mid
            elif mid**2 == num:
                return True
            else:
                left = mid+1
            
            # print(left, mid, right)