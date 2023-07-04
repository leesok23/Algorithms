# Version 1
def solution(absolutes, signs):
    count = 0
    for absolute, sign in zip(absolutes,signs):
        count += absolute if sign else absolute*(-1)
    return count


# Version 2
def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes,signs))
