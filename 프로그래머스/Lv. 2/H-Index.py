def solution(citations):
    citations.sort()
    count = 0
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            count += 1
    return count
