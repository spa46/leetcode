class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        visited = [False]*len(nums)
        
        def dfs(i):
            if not visited[i]:
                visited[i] = True
                return dfs(nums[i])+1
            else:
                return 0
        
        mmax = 0
        for i in range(len(nums)):
            mmax = max(mmax, dfs(i))
            
        return mmax