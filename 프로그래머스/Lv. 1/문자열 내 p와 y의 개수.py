def solution(s):
    p_cnt = s.lower().count('p')
    y_cnt = s.lower().count('y')

    return True if p_cnt == y_cnt else False
