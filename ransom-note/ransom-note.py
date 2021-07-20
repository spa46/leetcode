from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = defaultdict(int)
        for v in magazine:
            d[v] += 1
            
        for v in ransomNote:
            if v not in d:
                return False
            
            d[v] -= 1
            if d[v] <= 0:
                del d[v]
                
        return True
            
        