class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for j in range(len(matrix[0])):
            temp = []
            for i in range(len(matrix)):
                temp.append(matrix[i][j])
            result.append(temp)
        return result
