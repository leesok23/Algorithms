class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)-1):
            diagonal_move = min(abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]))
            vertical_move = abs(points[i][1]-points[i+1][1]) - diagonal_move
            horizontal_move = abs(points[i][0]-points[i+1][0]) - diagonal_move
            count += diagonal_move + vertical_move + horizontal_move
        return count
