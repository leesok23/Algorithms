def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        subarray = sorted(array[i-1:j])
        answer.append(subarray[k-1])
    return answer
