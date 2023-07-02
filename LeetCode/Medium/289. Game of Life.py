import copy
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #result = [[0 for x in range(len(board[0]))] for x in range(len(board))]
        #row, col = len(board), len(board[0])
        result = copy.deepcopy(board)
        
        result.insert(0, [0 for x in range(len(result[0]))])
        result.append([0 for x in range(len(result[0]))])
        for i in range(len(result)):
            result[i].insert(0, 0)
            result[i].append(0)
            
        for i in range(1, len(result)-1):
            for j in range(1, len(result[0])-1):
                n = result[i-1][j-1] + result[i-1][j] + result[i-1][j+1] + result[i][j-1] + result[i][j+1] + result[i+1][j-1] + result[i+1][j] + result[i+1][j+1]
                
                if result[i][j] == 1:
                    if n < 2 or n > 3:
                        board[i-1][j-1] = 0
                else:
                    if n == 3:
                        board[i-1][j-1] = 1
