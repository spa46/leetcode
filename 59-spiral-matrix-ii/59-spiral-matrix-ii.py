class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        arr = [[0]*n for _ in range(n)]
        
        cnt = 0
        i = 0
        while n>=1:
            
            j = i
            while j<n:
                arr[i][j] = cnt + 1
                cnt += 1
                j+=1
            j=i+1
            while j<n:
                arr[j][n-1] = cnt + 1
                cnt += 1
                j+=1

            j = n-2
            while j>=i:
                arr[n-1][j] = cnt + 1
                cnt += 1
                j-=1
                
            j = n-2
            while j>i:
                arr[j][i] = cnt + 1
                cnt += 1
                j-=1
            
            n -= 1
            i += 1
        return arr