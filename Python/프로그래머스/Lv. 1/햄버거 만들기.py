def solution(ingredient):
    temp = []
    count = 0
    for ingred in ingredient:
        temp.append(ingred)
        if temp[-4:] == [1,2,3,1]:
            count += 1
            for i in range(4):
                temp.pop()
    return count
