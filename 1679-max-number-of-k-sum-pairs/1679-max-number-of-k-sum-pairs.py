from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        
        for v in nums:
            d[v] += 1
        # print(d)
        cnt = 0
        # list_d = sorted(list(d.items()), key=lambda v: v[1], reverse=True)
        
        while nums:
            n = nums.pop(0)
            # print(d)
            if k-n in d:
                min_d = min(d[n], d[k-n])
                if n == k-n and d[n] == 1:
                    continue
                elif n == k-n:
                    min_d = min(d[n]//2, d[k-n]//2)
                    
                # print('HIT', d, (d[n]+1)//2, (d[k-n]+1)//2)
                
                cnt += min_d
                d[n] -= min_d
                d[k-n] -= min_d
                
                if d[n] <= 0:
                    d.pop(n)
                if d[k-n] <= 0:
                    d.pop(k-n)
                    
        return cnt
        