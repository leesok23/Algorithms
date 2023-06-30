# Version 1
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-low)//2 + (low%2 or high%2)


# Version 2
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2==1 or high%2==1:
            result = (high-low)//2 + 1
        else:
            result = (high-low)//2
        return result


# Version 3
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff == 0:
            if low % 2 == 0:
                n = 0
            else:
                n = 1
        elif diff == 1:
            n = 1
        elif (diff % 2 == 0 and low % 2 == 1) or diff % 2 == 1:
            n = diff // 2 + 1
        else:
            n = diff // 2

        return n
