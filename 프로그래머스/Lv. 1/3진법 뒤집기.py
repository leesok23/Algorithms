# Version 1
def solution(n):
    # 10진법 > 3진법
    temp = ''
    while n > 0:
        temp += str(n % 3) 
        n //= 3

    # return int(temp,3)

    # 3진법 > 10진법
    answer = 0
    for i, num in enumerate(temp[::-1]):
        answer += int(num) * (3**i)
    return answer


# Version 2
def solution(n):
    # 10진법 > 3진법
    new_n = ''
    while n > 0:
        new_n += str(n%3)
        n //= 3
    new_n = int(new_n)
    
    # 3진법 > 10진법
    answer, i = 0, 0
    while new_n > 0:
        answer += (new_n%10) * (3**i)
        new_n //= 10
        i += 1
    
    return answer
