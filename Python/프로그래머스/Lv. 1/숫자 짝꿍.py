from collections import Counter
def solution(X, Y):
    dict_X = Counter(X)
    dict_Y = Counter(Y)
    
    answer = []
    for key in dict_X.keys():
        if key in dict_Y.keys():
            answer += [key] * min(dict_X[key], dict_Y[key])
    
    answer = ''.join(sorted(answer, reverse=True)) if len(answer) > 0 else '-1'
    return answer[0] if answer[0] == '0' else answer
