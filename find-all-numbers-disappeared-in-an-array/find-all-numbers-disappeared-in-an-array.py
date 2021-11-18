class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        nums.sort()
        nums = list(set(nums))
        
        i = 1
        while i <= n:
            if not nums:
                arr.append(i)
            elif i != nums[0]:
                arr.append(i)
            else:
                nums.pop(0)
            i+=1
            
        return arr
                
            
            