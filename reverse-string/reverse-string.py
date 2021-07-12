class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        tmp = [v for v in s]
        
        for i in range(len(tmp)-1, -1, -1):
            j = len(s)-i-1
            # print(j, s[j], tmp[i])
            s[j] = tmp[i]
        
            