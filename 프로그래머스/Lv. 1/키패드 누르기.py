def solution(numbers, hand):
    def findPosition(number):
        phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        for row in range(len(phone)):
            for col in range(len(phone[0])):
                if phone[row][col] == number:
                    return [row, col]
                
    answer = ''
    cur_L, cur_R = [3,0], [3,2]
    for num in numbers:
        pos = findPosition(num)
        if pos[1] == 0:
            answer += 'L'
            cur_L = pos
        elif pos[1] == 2:
            answer += 'R'
            cur_R = pos
        else:
            if abs(pos[0]-cur_L[0])+abs(pos[1]-cur_L[1]) < abs(pos[0]-cur_R[0])+abs(pos[1]-cur_R[1]):
                answer += 'L'
                cur_L = pos
            elif abs(pos[0]-cur_L[0])+abs(pos[1]-cur_L[1]) > abs(pos[0]-cur_R[0])+abs(pos[1]-cur_R[1]):
                answer += 'R'
                cur_R = pos
            else:
                if hand == 'right':
                    answer += 'R'
                    cur_R = pos
                else:
                    answer += 'L'
                    cur_L = pos
    return answer
