class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_data = [0]*m
        col_data = [0]*n

        for indice in indices:
            row_data[indice[0]] += 1
            col_data[indice[1]] += 1

        count = 0
        for row in row_data:
            for col in col_data:
                if (row+col) % 2 != 0:
                    count += 1
        return count
