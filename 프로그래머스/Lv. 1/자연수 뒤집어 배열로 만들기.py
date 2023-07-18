# Version 1
def solution(n):
    answer = list(map(int, str(n)))
    return answer[::-1]


# Version 2
def solution(n):
    return [int(num) for num in str(n)][::-1]
