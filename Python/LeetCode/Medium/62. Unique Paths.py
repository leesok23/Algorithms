class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 and n == 0:
            return 0
        
        matrix = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            matrix[i][0] = 1
        for j in range(m):
            matrix[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                
        return matrix[n-1][m-1]
