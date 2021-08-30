class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = nums[0]
        for i in range(len(nums)):
            n = max(n, nums[i])
            
            if n<=0:
                if i == len(nums)-1:
                    return True
                return False
            
            n-=1
            # print(n)
        return True