import numpy as np

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        v = 0
        self.arr = nums
        self.cumsum = np.cumsum(nums)
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        diff = self.arr[index] - val
        self.cumsum[index:] -= diff
        self.arr[index] = val
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        l = 0
        if left > 0:
            l = self.cumsum[left -1]
        # print(l, self.cumsum[right])
        return self.cumsum[right] - l
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)