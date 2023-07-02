def solution(a, b, n):
    count = 0
    while n >= a:
        remain = n % a
        n //= a
        count += n*b
        n = n*b + remain
    return count
