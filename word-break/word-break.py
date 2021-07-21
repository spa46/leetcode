class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        starts = [0]
        for j in range(len(s)):
            for i in starts:
                if s[i:j+1] in wordDict:
                    starts.append(j+1)
                    break
        return starts[-1] == len(s)