# Version 1
def solution(n):
    answer = 0
    num = 1
    while num < (n**0.5):
        if n % num == 0:
            answer += num + n//num
        num += 1
    if num**2 == n:
        answer += num
    return answer


# Version 2
def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            answer += i
            if i**2 != n:
                answer += n//i
    return answer
