def solution(sizes):
    max1, max2 = 0, 0
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        max1 = max(max1, size[0])
        max2 = max(max2, size[1])
        
    return max1 * max2
