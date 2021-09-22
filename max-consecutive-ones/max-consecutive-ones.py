class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        i=0
        while i < len(nums):
            out = 0
            while(i<len(nums) and nums[i] == 1):
                out += 1
                i += 1
            ans = max(ans, out)
            out = 0
            while(i<len(nums) and nums[i] == 0):
                i += 1
            
            # print(i, ans)
            
        return ans