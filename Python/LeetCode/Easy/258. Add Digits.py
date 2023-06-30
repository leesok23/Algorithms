class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num // 10 == 0:
            return num
        
        n = 0
        while True:
            n += num % 10
            if num // 10 > 0:
                num = num // 10
            else:
                num = n
                n = 0
                if num // 10 == 0:
                    return num
