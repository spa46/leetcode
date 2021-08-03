class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        w = len(matrix)
        h = len(matrix[0])
                
        visited = [[False]*h for _ in range(w)]
        out = []
        
        def traverse(curr, d):
            x = curr[0]; y = curr[1]
            if 0<=x<w and 0<=y<h and not visited[x][y]:
                out.append(matrix[x][y])
                visited[x][y] = True
                if d == 0:
                    traverse((x, y+1), 0)
                    traverse((x+1, y), 1)
                    traverse((x, y-1), 2)
                    traverse((x-1, y), 3)
                elif d == 1:
                    traverse((x+1, y), 1)
                    traverse((x, y-1), 2)
                    traverse((x-1, y), 3)
                    traverse((x, y+1), 0)
                elif d == 2:
                    traverse((x, y-1), 2)
                    traverse((x-1, y), 3)
                    traverse((x, y+1), 0)
                    traverse((x+1, y), 1)
                elif d == 3:
                    traverse((x-1, y), 3)
                    traverse((x, y+1), 0)
                    traverse((x+1, y), 1)
                    traverse((x, y-1), 2)
                
        traverse((0,0), 0)
        return out