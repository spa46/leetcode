class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        t = text.split(' ')
        len_text = len(t)
        bc = list(brokenLetters)
        cntw = 0
        for v in t:
            for c in v:
                if c in bc:
                    cntw += 1
                    break
                # print(c, v)
                
        # print(len_text-cntw)
        return len_text-cntw