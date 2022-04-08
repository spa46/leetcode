from collections import defaultdict
from math import comb

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        d = defaultdict(int)
        
        for v in arr:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1
        
        d = sorted(d.items())
        
        cnt = 0
        len_d = len(d)
        for i in range(len_d):
            for j in range(i, len_d):
                for k in range(j, len_d):
                    sum = d[i][0]+d[j][0]+d[k][0]
                    if sum == target:
                        tmp = 0
                        if d[i][0] == d[j][0] and d[j][0] == d[k][0]:
                            if d[i][1]<3:
                                continue
                            tmp = comb(d[i][1],3)
                        elif d[i][0] == d[j][0]:
                            if d[i][1]<2:
                                continue
                            tmp = comb(d[i][1],2) * d[k][1]
                        elif d[j][0] == d[k][0]:
                            if d[j][1]<2:
                                continue
                            tmp = comb(d[j][1],2) * d[i][1]
                        else:
                            tmp = d[i][1]*d[j][1]*d[k][1]
                        # print(i,j,k, sum, tmp)
                        cnt += tmp
                        
                    elif sum > target:
                        break
                    # print(i,j,k, sum)
        
        return cnt%1000000007
    