class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # [0,0], [1,1], [2,2]: row = col
        # [0,2], [1,1], [2,0]: row + col = 2
        # three have all rows in a col
        # three have all cols in a row
        player_score = [[0] * 8 for _ in range(2)]
        for i, move in enumerate(moves):
            r, c = move
            if i % 2 == 0:
                player = 0
            else:
                player = 1
            
            if r == c:
                player_score[player][6] += 1
            if r + c == 2:
                player_score[player][7] += 1

            player_score[player][r] += 1
            player_score[player][c+3] += 1

        if 3 in player_score[0]:
            return 'A'
        elif 3 in player_score[1]:
            return 'B'
        
        return 'Draw' if len(moves) == 9 else 'Pending'
