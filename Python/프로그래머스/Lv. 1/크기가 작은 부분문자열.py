def solution(t, p):
    len_p = len(p)
    count = 0
    for i in range(len(t)-len_p+1):
        if int(t[i:i+len_p]) <= int(p):
            count += 1
    return count
