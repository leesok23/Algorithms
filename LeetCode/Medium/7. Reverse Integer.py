class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
            x = x * (-1)
        
        num = 0
        while x > 0:
            temp = x % 10
            num = num * 10 + temp
            x = x // 10
        
        if isNegative:
            num = num * (-1)
        if num < (-1) * 2 ** 31 or num > 2 ** 31 - 1:
            return 0
        return num
