# Version 1
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)

    return answer


# Version 2
def solution(arr1, arr2):
    return [[c+d for c, d in zip(a,b)] for a,b in zip(arr1,arr2)]
