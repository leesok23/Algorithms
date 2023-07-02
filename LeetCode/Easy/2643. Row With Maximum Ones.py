class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result = []
        count_one = 0
        ind_row = 0
        for row in range(len(mat)):
            if mat[row].count(1) > count_one:
                count_one = mat[row].count(1)
                ind_row = row
        return [ind_row, count_one]
