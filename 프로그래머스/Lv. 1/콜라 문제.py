def solution(a, b, n):
    answer = 0
    while n >= a:
        receive = (n // a) * b
        remain = n % a
        answer += receive
        n = receive + remain
    return answer
