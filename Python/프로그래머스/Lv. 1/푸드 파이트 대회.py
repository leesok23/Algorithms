def solution(food):
    result = '0'
    for i in range(len(food)-1, 0, -1):
        num_food = food[i] // 2
        result = str(i)*num_food + result + str(i)*num_food
    return result
