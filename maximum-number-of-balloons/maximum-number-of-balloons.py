from collections import defaultdict
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        
        d = defaultdict(int)
        
        for v in text:
            if v in ('b','a','l','o', 'n'):
                d[v] += 1
            
        d['l'] = d['l']//2
        d['o'] = d['o']//2
        
        return min (d['b'],d['a'],d['l'],d['o'], d['n'])