# Version 1
def solution(d, budget):
    d.sort()
    cum = 0
    for i, money in enumerate(d):
        cum += money
        if cum > budget:
            return i
    return len(d)


# Version 2
def solution(d, budget):
    d.sort()
    for i in range(len(d),-1,-1):
        if sum(d[:i]) <= budget:
            return i


# Version 3
def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)
