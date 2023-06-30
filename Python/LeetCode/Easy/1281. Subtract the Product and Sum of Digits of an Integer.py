class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod_n, sum_n = 1, 0
        while n > 0:
            temp = n % 10
            prod_n *= temp
            sum_n += temp
            n //= 10
        return prod_n - sum_n
