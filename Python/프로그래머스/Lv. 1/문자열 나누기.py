def solution(s):
    answer, count1, count2 = 0, 0, 0
    first_letter = s[0]
    i = 0
    while i < len(s):
        if s[i] == first_letter:
            count1 += 1
        else:
            count2 += 1
            
        if count1 == count2:
            answer += 1
            count1, count2 = 0, 0
            if i < len(s)-1:
                first_letter = s[i+1]
        elif i == len(s)-1:
            answer += 1
        i += 1
    return answer
