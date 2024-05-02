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


# Version 3
def solution(n, m):
    if n > m:
        n, m = m, n
        
    # 최대공약수
    for i in range(n,0,-1):
        if m % i == 0 and n % i == 0:
            common_divisor = i
            break
    
    # 최소공배수
    for i in range(1,m+1):
        if m*i % n == 0:
            common_multiple = m*i
            break
    
    return [common_divisor, common_multiple]
