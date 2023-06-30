class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        
        grid.insert(0, [0 for x in range(len(grid[0]))])
        grid.append([0 for x in range(len(grid[0]))])
        
        n = 0
        for i in range(len(grid)):
            grid[i].insert(0, 0)
            grid[i].append(0)
            for j in range(len(grid[i])-1):
                if grid[i][j] != grid[i][j+1]:
                    n += 1
                if i > 0:
                    if grid[i][j] != grid[i-1][j]:
                        n += 1
        
        return n
