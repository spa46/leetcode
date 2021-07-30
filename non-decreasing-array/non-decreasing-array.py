class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums)<3:
            return True
        
        cnt = 0
        for i in range(2, len(nums)):
            a = nums[i-2]
            b = nums[i-1]
            c = nums[i]

            if a<=b:
                if b>c:
                    if a>c:
                        nums[i] = b
                    elif a<=c:
                        nums[i-1] = c
                    cnt += 1
            
            elif a>b:
                if b>c:
                    return False
                elif b<c:
                    if a<=c:
                        nums[i-1] = c
                    elif a>c:
                        nums[i-2] = b
                    cnt += 1
            # print(nums)
        if cnt > 1:
            return False

        return True
                    
                    