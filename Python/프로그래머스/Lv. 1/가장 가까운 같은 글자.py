def solution(s):
    dict_s = {}
    answer = []
    for i in range(len(s)):
        if s[i] not in dict_s:
            dict_s[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - dict_s[s[i]])
            dict_s[s[i]] = i
    return answer
