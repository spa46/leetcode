class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        
        for v in s:
            if v in '({[':
                stk.append(v)
            else:
                if not stk:
                    return False
                
                if stk[-1] == '(' and v == ')':
                    stk.pop()
                elif stk[-1] == '[' and v ==']':
                    stk.pop()
                elif stk[-1] == '{' and v == '}':
                    stk.pop()
                else:
                    return False
            # print(stk)
        if stk:
            return False
        
        return True