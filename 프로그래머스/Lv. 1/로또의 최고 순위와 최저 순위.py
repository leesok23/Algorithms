# Version 1
def solution(lottos, win_nums):
    count_zero = lottos.count(0)
    count_match = len(win_nums) - len(set(win_nums)-set(lottos))

    min_prize = 7 - count_match if count_match >= 1 else 6
    max_prize = 7 - (count_match+count_zero) if count_match+count_zero >= 1 else 6
    
    return [max_prize, min_prize]


# Version 2
def solution(lottos, win_nums):
    rank=[6, 6, 5, 4, 3, 2, 1]

    count_zero = lottos.count(0)
    count_match = 0
    for num in lottos:
        if num in win_nums:
            count_match += 1
            
    return rank[count_zero + count_match], rank[count_match]
