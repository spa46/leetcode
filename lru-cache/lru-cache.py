class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.stack = []
        self.d = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        else:
            self.stack.remove(key)
            self.stack.append(key)
            return self.d[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.stack.remove(key)
            
        if len(self.stack) >= self.cap:
            k = self.stack[0]
            del self.stack[0]
            del self.d[k]
            
        self.d[key] = value
        self.stack.append(key)
        # print(self.d)
        # print(self.stack)
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)