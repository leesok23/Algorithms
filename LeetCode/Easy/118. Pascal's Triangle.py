class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(len(result[i-1])-1):
                temp.append(result[i-1][j] + result[i-1][j+1])
            temp.append(1)
            result.append(temp)
        
        return result
