def solution(s, skip, index):
    alpha = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in skip]
    # alpha_dict = {a: ind for ind, a in enumerate(alpha)}
    
    answer = ''
    for string in s:
        ind = alpha.index(string)+index
        ind %= len(alpha)
        answer += alpha[ind]
    return answer
