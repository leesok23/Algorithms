# Version 1
def solution(n):
    return sum([int(num) for num in str(n)])


# Version 2
def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n //= 10
    return answer
