def solution(babbling):
    count = 0
    for babb in babbling:
        temp = ''
        isTrue = True
        while len(babb) > 0:
            if babb[:2] == 'ye' and temp != 'ye':
                temp = babb[:2]
                babb = babb[2:]
            elif babb[:2] == 'ma' and temp != 'ma':
                temp = babb[:2]
                babb = babb[2:]
            elif babb[:3] == 'aya' and temp != 'aya':
                temp = babb[:3]
                babb = babb[3:]
            elif babb[:3] == 'woo' and temp != 'woo':
                temp = babb[:3]
                babb = babb[3:]
            else:
                isTrue = False
                break
        if isTrue:
            count += 1
    return count
