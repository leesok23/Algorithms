def solution(number):
    count = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    count += 1
    return count
