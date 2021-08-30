class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0, len(height)-1
        
        mmax = 0
        while i<j:
            a = height[i]
            b = height[j]
            mmax = max(mmax, min(a, b) * (j-i))
            if a<b:
                i+=1
            else:
                j-=1
            print(mmax)
        
        return mmax