class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        indRow = []
        indCol = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    indRow.append(i)
                    indCol.append(j)
                    
        for i in indRow:
            for j in range(col):
                matrix[i][j] = 0
        for i in range(row):
            for j in indCol:
                matrix[i][j] = 0
