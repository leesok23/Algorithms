def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    length = len(score)
    i = 1
    while length >= m*i:
        answer += score[i*m-1] * m
        i += 1
    return answer
