def solution(s):
    words = {}
    answer = []
    for i in range(len(s)):
        if s[i] not in words:
            answer.append(-1)
        else:
            answer.append(i-words[s[i]])
        words[s[i]] = i
    return answer
