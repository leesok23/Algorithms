# Version 1
def solution(s):
    if s[0] == '+':
        return int(s[1:])
    elif s[0] == '-':
        return -1*int(s[1:])
    else:
        return int(s)


# Version 2
def solution(s):
    return int(s)
