def solution(n):
    temp = ''
    while n > 0:
        temp += str(n % 3) 
        n //= 3

    # return int(temp,3)
    
    answer = 0
    for i, num in enumerate(temp[::-1]):
        answer += int(num) * (3**i)
    return answer
