class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i=0
        j=int(c**(1/2.0))
        
        while i<=j:
            ii,jj = i*i, j*j
            ij = ii + jj
            # print(i,j, ij)
            
            if ij > c:
                j-=1
            elif ij < c:
                i+=1
            else:
                return True
        return False