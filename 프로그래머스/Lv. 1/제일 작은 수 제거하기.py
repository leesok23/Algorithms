# Version 1
def solution(arr):
    min_arr = min(arr)
    arr.remove(min_arr)
    return arr if len(arr)>0 else [-1]


# Version 2
def solution(arr):
    min_arr = min(arr)
    answer = [i for i in arr if i > min_arr]
    return answer if len(answer)>0 else [-1]
