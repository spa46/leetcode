from collections import Counter
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        freq = []
        arr = []
        cnt = 0
        c = Counter(s)
        n=1
        print(c.most_common())
        for _,v in sorted(c.most_common(), key=lambda v:v[1]):
            arr += [i for i in range(n, v)]
            if v not in freq:
                freq.append(v)
            else:
                if not arr:
                    cnt += v
                    continue
                else:
                    last = arr.pop()
                    cnt += v-last
                    freq.append([last])
            n = v+1
            print(v, freq, arr)
        return cnt
        