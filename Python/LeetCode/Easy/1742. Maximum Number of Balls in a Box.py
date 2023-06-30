class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def boxNumber(x):
            result = 0
            while x > 0:
                result += x % 10
                x //= 10
            return result

        dict = {}
        for ball in range(lowLimit, highLimit+1):
            box_number = boxNumber(ball)
            if box_number not in dict:
                dict[box_number] = 1
            else:
                dict[box_number] += 1
        
        return max(dict.values())
