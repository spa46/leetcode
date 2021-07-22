class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.arr:
            return -1
        
        return self.arr[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.arr)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()