def solution(s, n):
    answer = ''
    len_alpha = ord('z') - ord('a') + 1
    for i in s:
        if i == ' ':
            answer += i
        elif i.islower():
            answer += chr((ord(i)+n-ord('a'))%len_alpha+ord('a'))
        else:
            answer += chr((ord(i)+n-ord('A'))%len_alpha+ord('A'))
    return answer
