class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        w = len(matrix[0])
        h = len(matrix)
        
        for i in range(h/2):
            j = h-i-1
            tmp = matrix[j]
            matrix[j] = matrix[i]
            matrix[i] = tmp
        
        for i in range(h):
            for j in range(i+1, w):
                tmp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tmp
        
        return matrix