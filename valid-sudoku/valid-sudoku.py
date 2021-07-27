import numpy as np

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        b = np.array(board)
        print(b)
        # print(b[0:3,0:3])
        # print(b[3:6,3:6])
        
        # print(set(b[0,:]))
        # print(b[:,0])
        for i in range(len(b)):
            ur, cr = np.unique(b[i,:], return_counts=True)
            uc, cc = np.unique(b[:,i], return_counts=True)
            len_r = len(ur[cr > 1])
            len_c = len(uc[cc > 1])
            if len_r > 1 or len_c > 1:
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                u, c = np.unique(b[i:i+3,j:j+3], return_counts=True)
                len_u = len(u[c > 1])
                if len_u > 1:
                    return False
        
        return True
        