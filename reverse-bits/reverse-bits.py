class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        bn = format(n, '#034b')[2:]
        
        return int(bn[::-1], 2)