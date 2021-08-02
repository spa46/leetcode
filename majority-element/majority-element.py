from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        len_n = len(nums)
        
        mmax = 0
        maxv = 0
        
        for v in nums:
            d[v] += 1
            
            if mmax < d[v]:
                mmax = d[v]
                maxv = v
            
            
        return maxv
        