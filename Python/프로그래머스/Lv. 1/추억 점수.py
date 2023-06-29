def solution(name, yearning, photo):
    name_yearning = {x: y for x, y in zip(name, yearning)}
    answer = []
    for p in photo:
        count = 0
        for i in range(len(p)):
            if p[i] in name_yearning:
                count += name_yearning[p[i]]
        answer.append(count)
    return answer
