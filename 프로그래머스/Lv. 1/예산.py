def solution(d, budget):
    d.sort()
    cum = 0
    for i, money in enumerate(d):
        cum += money
        if cum > budget:
            return i
    return len(d)
