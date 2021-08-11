class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        out = []
        def dfs(p, r, pos):
            l = 3 if len(r)>=3 else len(r)
            if pos < 4:
                for i in range(l):
                    np = r[0:i+1]
                    
                    if len(np)>1 and np[0] == '0':
                        continue
                    
                    np = int(np)
                    if 0<=np<=255:
                        
                        dfs(p + [np], r[i+1:], pos+1)
            else:
                if not r:
                    ip = '.'.join(map(str, p))
                    if ip not in out:
                        out.append(ip)
                #join
        
        if not s:
            return []
        
        for i in range(3):
            np = s[0:i+1]
            if len(np)>1 and np[0] == '0':
                continue
            
            np = int(np)
            if 0<=np<=255:
                dfs([np], s[i+1:], 1)
                
        return out
            