# Version 1
def solution(s):
    if len(s) % 2 == 0:
        answer = s[len(s)//2-1:len(s)//2+1]
    else:
        answer = s[len(s)//2]
    return answer


# Version 2
def solution(s):
    answer = s[(len(s)-1)//2:len(s)//2+1]
    return answer
