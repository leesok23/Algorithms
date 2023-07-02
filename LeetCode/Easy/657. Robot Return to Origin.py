class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count_updown, count_leftright = 0, 0
        for move in moves:
            if move == 'U':
                count_updown += 1
            elif move == 'D':
                count_updown -= 1
            elif move == 'L':
                count_leftright += 1
            else:
                count_leftright -= 1
        
        return True if count_updown == 0 and count_leftright == 0 else False
