from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        arr = sorted(c.values())

        has_odd = False
        longest = 0
        for v in arr:
            if v%2 == 1:
                if has_odd:
                    v-=1
                else:
                    has_odd = True
            # print(v)
            longest += v
            
        return longest