def solution(k, score):
    answer = []
    tmp = []
    for i in range(len(score)):
        tmp.append(score[i])
        tmp.sort()
        if len(tmp) > k:
            tmp.pop(0)
        answer.append(tmp[0])
    return answer
