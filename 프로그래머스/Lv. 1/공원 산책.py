def solution(park, routes):
    def findObstacle(park, row, col, direction, distance):
        for i in range(1,distance+1):
            if direction == 'E':
                if col+i >= len(park[0]) or park[row][col+i] == 'X':
                    return False
            elif direction == 'W':
                if col-i < 0 or park[row][col-i] == 'X':
                    return False
            elif direction == 'S':
                if row+i >= len(park) or park[row+i][col] == 'X':
                    return False
            elif direction == 'N':
                if row-i < 0 or park[row-i][col] == 'X':
                    return False
        return True
    
    def findStart(park):
        for i in range(len(park)):
            for j in range(len(park[0])):
                if park[i][j] == 'S':
                    return [i,j]
                    
    location = findStart(park)
    for route in routes:
        direction = route.split(' ')[0]
        distance = int(route.split(' ')[1])
        if findObstacle(park, location[0], location[1], direction, distance):
            if direction == 'E':
                location[1] += distance
            elif direction == 'W':
                location[1] -= distance
            elif direction == 'S':
                location[0] += distance
            else:
                location[0] -= distance
    return location
