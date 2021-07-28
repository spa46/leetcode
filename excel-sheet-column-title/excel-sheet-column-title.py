class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        c = ['Z','A','B','C','D','E',
             'F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T',
             'U','V','W','X','Y','Z']
        

        def div(n):
            if n <= 26:
                return c[n]
            else:
                d = n / 26
                r = n % 26
                if r == 0:
                    d -= 1
                print(n, d, r)
                return div(d) + c[r]
            
        return div(columnNumber)