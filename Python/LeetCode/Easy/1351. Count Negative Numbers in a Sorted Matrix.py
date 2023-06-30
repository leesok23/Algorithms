class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = 0
        for i in range(len(grid)):
            if grid[i][0] < 0:
                n += len(grid[0]) * (len(grid) - i)
                break
            else:
                for j in range(len(grid[0])):
                    if grid[i][j] < 0:
                        n += len(grid[0]) - j
                        break
        return n
