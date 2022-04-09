from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        
        for v in nums:
            if v in d:
                d[v] += 1
            else:
                d[v] = 0
        
        sd = sorted(d.items(), key=lambda v: v[1],reverse=True)
        ans = [v[0] for v in sd[:k]]
            
        return ans