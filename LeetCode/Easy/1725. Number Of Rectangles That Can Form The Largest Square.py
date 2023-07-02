class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        len_square = []
        for rectangle in rectangles:
            min_len = min(rectangle)
            len_square.append(min_len)
        return len_square.count(max(len_square))
