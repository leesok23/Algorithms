class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(0, len(grid)-2):
            result_temp = []
            for j in range(0, len(grid[0])-2):
                temp = grid[i][j]
                for k in range(3):
                    temp = max(max(grid[i+k][j:j+3]), temp)
                result_temp.append(temp)
            result.append(result_temp)
        return result
