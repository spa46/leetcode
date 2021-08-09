class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        d = {}
        for i, v in enumerate(sorted(nums)):
            if v not in d:
                d[v] = i
            
        arr = []
        for v in nums:
            arr.append(d[v])
            
        return arr