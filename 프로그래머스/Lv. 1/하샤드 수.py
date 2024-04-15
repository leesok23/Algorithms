# Version 1
def solution(x):
    x_list = list(str(x))
    count = 0
    for num in x_list:
        count += int(num)
    return True if x%count==0 else False


# Version 2
def solution(x):
    sum_x = sum([int(num) for num in str(x)])
    return True if x%sum_x==0 else False
