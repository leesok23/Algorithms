def solution(n):
    n = n**0.5
    return (n+1)**2 if n%1==0 else -1
