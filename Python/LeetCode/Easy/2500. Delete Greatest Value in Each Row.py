class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        while len(grid[0]) > 0:
            temp = []
            for i in range(len(grid)):
                max_grid = max(grid[i])
                temp.append(max_grid)
                grid[i].remove(max_grid)
            result += max(temp)
        return result
