# Version 1
def solution(n):
    return '수박'*(n//2) + '수'*(n%2)


# Version 2
def solution(n):
    answer = '수박'*n
    return answer[:n]
