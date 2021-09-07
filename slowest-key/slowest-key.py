class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        
        pindex = [(0, keysPressed[0])]
        rt = releaseTimes[0]
        
        for i in range(1, len(releaseTimes)):
            t = releaseTimes[i]-releaseTimes[i-1]
            if rt < t:
                rt = t
                pindex = [(i, keysPressed[i])]
            elif rt == t:
                pindex.append((i, keysPressed[i]))
        
        pindex.sort(key=lambda v:v[1])

        return pindex[-1][-1]