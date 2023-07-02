class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        numFive = 0
        while n > 4:
            numFive += n // 5
            n = n // 5
        return numFive
