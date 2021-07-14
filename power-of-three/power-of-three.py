class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n>=3 and n%3==0:
            n /= 3
        
        if n == 1:
            return True
        
        return False