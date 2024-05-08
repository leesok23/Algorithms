# Version 1
def solution(name, yearning, photo):
    name_yearning = {x: y for x, y in zip(name, yearning)}
    # name_yearning = dict(zip(name,yearning))
    answer = []
    for ph in photo:
        count = 0
        for p in ph:
            if p in name_yearning:
                count += name_yearning[p]
        answer.append(count)
    return answer


# Version 2
def solution(name, yearning, photo):
    answer = []
    name_yearning = dict(zip(name,yearning))
    for ph in photo:
        answer.append(sum(map(lambda x: name_yearning[x] if x in name_yearning else 0, ph)))
    return answer
