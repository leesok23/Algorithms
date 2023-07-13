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
