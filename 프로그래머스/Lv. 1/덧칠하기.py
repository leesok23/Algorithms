def solution(n, m, section):
    start = section[0]
    end = section[0] + m - 1
    count = 1
    for i in range(len(section)):
        if start <= section[i] <= end:
            continue
        else:
            start = section[i]
            end = min(start+m-1, n)
            count += 1
    return count
