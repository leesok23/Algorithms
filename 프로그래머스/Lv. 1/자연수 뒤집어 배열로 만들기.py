# Version 1
def solution(n):
    answer = list(map(int, str(n)))
    return answer[::-1]


# Version 2
def solution(n):
    return [int(num) for num in str(n)][::-1]


# Version 3
def solution(n):
    answer = []
    while n > 0:
        answer.append(n%10)
        n //= 10
    return answer
