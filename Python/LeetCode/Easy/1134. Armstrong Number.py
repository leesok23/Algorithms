class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        result = 0
        for i in list(str(n)):
            result += int(i)**k
        return result == n
