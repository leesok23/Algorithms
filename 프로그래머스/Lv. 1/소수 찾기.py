# Version 1
def solution(n):
    def isPrime(num):
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    return sum([isPrime(m) for m in range(2,n+1)])
    

# Version 2
def solution(n):
    if n == 2:
        return 1
    count = 0
    for num in range(3,n+1,2):
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                count += 1
                break
    return n-count-(n//2)
