class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nRow, nCol = len(nums), len(nums[0])
        if r * c != nRow * nCol:
            return nums
        
        mat = [[] for i in range(r)]
        n = 0
        for i in range(nRow):
            for j in range(nCol):
                if len(mat[n]) == c:
                    n += 1
                mat[n].append(nums[i][j])
                
        return mat
