def solution(sizes):
    row, col = 0, 0
    for a, b in sizes:
        if b > a:
            a, b = b, a
        row = max(a,row)
        col = max(b,col)
    return row * col
