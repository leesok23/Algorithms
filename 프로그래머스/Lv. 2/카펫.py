def solution(brown, yellow):
    total = brown + yellow
    for num in range(3, total**2+1):
        if total % num == 0 and (total//num-2)*(num-2) == yellow:
            return [total//num, num]
