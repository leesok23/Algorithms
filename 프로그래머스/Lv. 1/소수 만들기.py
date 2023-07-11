def solution(nums):
    def checkPrime(num):
        for n in range(2,int(num**0.5)+1):
            if num % n == 0:
                return False
        return True
    
    count = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                count += checkPrime(nums[i]+nums[j]+nums[k])
    return count
