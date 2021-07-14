class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        arr = []
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        for j in range(len(num2)-1,-1,-1):
            digit = (len(num2)-1)-j

            for i in range(len(num1)-1,-1,-1):
                n = int(num1[i])*int(num2[j])

                if len(arr)>digit:
                    arr[digit] += n
                else:
                    arr.append(n)
                
                # print(arr, digit, n)
                digit += 1
        
        c = 0
        for i in range(len(arr)):
            arr[i] += c
            c = arr[i]//10
            arr[i] = str(arr[i]%10)
            # print(arr[i], c)
        
        if c != 0:
            arr.append(str(c))
        
        return ''.join(arr[::-1])