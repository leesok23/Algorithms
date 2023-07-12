def solution(x):
    x_list = list(str(x))
    count = 0
    for num in x_list:
        count += int(num)
    return True if x%count==0 else False
