# Version 1
def solution(x, n):
    return [i*x for i in range(1,n+1)]


# Version 2
def solution(x, n):
    answer = [x]
    i = 1
    while i < n:
        answer.append(answer[-1]+x)
        i += 1
    return answer
