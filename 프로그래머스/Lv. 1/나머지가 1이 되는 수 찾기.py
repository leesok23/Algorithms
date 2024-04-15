# Version 1
def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x


# Version 2
def solution(n):
    answer = 2
    while answer < n:
        if n % answer == 1:
            return answer
        answer += 1
