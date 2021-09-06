class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        m = s
        
        i=0
        while i < len(s):
            f,r = s[:i], s[i:]
            for j in range(0, len(r)-1):
                t = r[j+1:] + r[:j] + r[j]
                m = min(m, f+t)
                # print(f, t)
            i+=1
            # print(m)
            s = m
            if k == 1:
                break
                
        return m