# Version 1
def solution(num):
    answer = 0
    while num > 1 and answer <= 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 + 1
        answer += 1

    return answer if answer <= 500 else -1


# Version 2
def solution(num):
    n = 0
    while n < 500:
        if num == 1:
            return n
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 + 1
        n += 1
    return -1
