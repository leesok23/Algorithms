def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)):
        if i < k:
            temp.append(score[i])
        elif i >= k and score[i] > temp[-1]:
            temp.pop()
            temp.append(score[i])
        temp.sort(reverse=True)
        answer.append(temp[-1])
            
    return answer
