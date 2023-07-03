# Version 1
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


# Version 2
def solution(left, right):
    def calculateDivisor(number):
        count = 0
        for num in range(1,int(number**0.5)+1):
            if number % num == 0:
                if num**2 == number:
                    count += 1
                else:
                    count += 2
        return count

    answer = 0
    for num in range(left, right+1):
        if calculateDivisor(num) % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer
