# Version 1
def solution(number, limit, power):
    iron = []
    for num in range(1,number+1):
        count = []
        for i in range(1,int(num**0.5)+1):
            if num % i == 0:
                count += [i, num//i]
            
        count = len(set(count))
        if count <= limit:
            iron.append(count)
        else:
            iron.append(power)
    return sum(iron)


# Version 2
def solution(number, limit, power):
    answer = []
    for num in range(1,number+1):
        count = 0
        for i in range(1,int(num**0.5)+1):
            if num % i == 0:
                if i**2 != num:
                    count += 2
                else:
                    count += 1
        if count > limit:
            answer.append(power)
        else:
            answer.append(count)
    return sum(answer)
