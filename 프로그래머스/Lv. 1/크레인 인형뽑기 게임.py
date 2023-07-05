def solution(board, moves):
    basket = []
    pos = [0] * len(board)
    count = 0
    for move in moves:
        i = pos[move-1]
        while i < len(board):
            if board[i][move-1] == 0:
                i += 1
            elif board[i][move-1] != 0:
                if len(basket) == 0 or basket[-1] != board[i][move-1]:
                    basket.append(board[i][move-1])
                else:
                    basket.pop()
                    count += 1
                board[i][move-1] = 0
                pos[move-1] = i
                break
    return count * 2
