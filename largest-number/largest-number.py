class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if max(nums) <= 0:
            return '0'
        
        nums = list(map(str, nums))
        
        for _ in range(len(nums)-1):
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < nums[i+1] + nums[i]:
                    nums[i:i+2] = [nums[i+1], nums[i]]
        
        return ''.join(nums)