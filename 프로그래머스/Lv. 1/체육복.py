def solution(n, lost, reserve):
    lost_update = set(lost) - set(reserve)
    reserve_update = set(reserve) - set(lost)
    for l in lost_update:
        if l-1 in reserve_update:
            reserve_update.remove(l-1)
        elif l+1 in reserve_update:
            reserve_update.remove(l+1)
        else:
            n -= 1
            
    return n
