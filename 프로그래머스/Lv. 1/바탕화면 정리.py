def solution(wallpaper):
    x, y = [], []
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == '#':
                x.append(row)
                y.append(col)
    return [min(x), min(y), max(x)+1, max(y)+1]
