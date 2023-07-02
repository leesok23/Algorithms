def solution(sequence, k):
    left, right = 0, 0
    sum_seq = sequence[left]
    min_len = 12312414123412
    while left <= right < len(sequence):
        if sum_seq < k:
            right += 1
            if right < len(sequence):
                sum_seq += sequence[right]
        elif sum_seq > k:
            sum_seq -= sequence[left]
            left += 1
        else:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                answer = [left, right]
            sum_seq -= sequence[left]
            left += 1
    return answer
