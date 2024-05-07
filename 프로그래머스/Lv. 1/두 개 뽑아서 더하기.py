# Version 1
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
            
    return sorted(list(set(answer)))


# Version 2
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            two_numbers = numbers[i]+numbers[j]
            if two_numbers not in answer:
                answer.append(two_numbers)
    return sorted(answer)
