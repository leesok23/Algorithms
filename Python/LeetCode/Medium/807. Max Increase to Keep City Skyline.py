class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        topBottom, leftRight = [0 for i in range(col)], []
        for i in range(row):
            leftRight.append(max(grid[i]))
            for j in range(col):
                topBottom[j] = max(topBottom[j], grid[i][j])
                
        n = 0
        for i in range(row):
            for j in range(col):
                if topBottom[j] < leftRight[i]:
                    n += topBottom[j] - grid[i][j]
                else:
                    n += leftRight[i] - grid[i][j]
                    
        return n
