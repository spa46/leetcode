class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = [0]*(len(nums))
        
        
        
        for i in range(len(nums)):
            s = nums[i]
            for j in range(i+1, i+s+1):
                if j < len(nums):
                    if cnt[j] <= 0:
                        cnt[j] = cnt[i] + 1
                    if j == len(nums)-1:
                        return cnt[-1]
                
                
        return 0