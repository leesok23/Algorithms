# Version 1
def solution(n, m):
    for num in range(min(n,m),0,-1):
        if n%num==0 and m%num==0:
            common_divisor = num
            break
    return [common_divisor,n*m//common_divisor]


# Version 2
def solution(n, m):
    for num in range(min(n,m),0,-1):
        if n%num==0 and m%num==0:
            common_divisor = num
            break
    for num in range(min(n,m),n*m+1):
        if num%n==0 and num%m==0:
            common_multiple = num
            break
    return [common_divisor,common_multiple]
