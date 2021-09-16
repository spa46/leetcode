class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def cal(s, i):
            sum = 0
            op = '+'
            n = '0'
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                    continue
                    
                if s[i] == '(':
                    sum2, i = cal(s, i+1)
                    n = str(sum2)
                elif s[i] == ')':
                    t = int(n)
                    if op == '-':
                        t = -1*t

                    sum += t
                    return sum, i
                elif s[i] == '+' or s[i] == '-':
                    t = int(n)
                    if op == '-':
                        t = -1*t
                    
                    sum += t
                    
                    if s[i] == '+':
                        op = '+'
                    else:
                        op = '-'
                    
                    n = '0'
                else:
                    n += s[i]

                i += 1
                # print(i, sum)
            
            t = int(n)
            if op == '-':
                t = -1*t

            sum += t
            
            return sum, i
                
        ans, _ = cal(s, 0)
        return ans