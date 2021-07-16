class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        arr = [[1]*n]
        arr += [[1]+[0]*(n-1)  for _ in range(m-1)]

        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] += arr[i-1][j] + arr[i][j-1]
        
        return arr[m-1][n-1]