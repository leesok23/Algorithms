class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1, 1, 2]
        if n < 3:
            return result[n]
        
        for i in range(3, n+1):
            result.append(result[i-1] + result[i-2])
        
        return result[-1]
