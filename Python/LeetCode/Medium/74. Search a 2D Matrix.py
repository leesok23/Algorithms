class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix in [[], [[]]]:
            return False
        
        l, h = 0, len(matrix) - 1
        while l <= h:
            m = (l + h) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                l = m + 1
            else:
                h = m - 1
                
        for j in range(len(matrix[h])):
            if matrix[h][j] == target:
                return True
            
        return False
