class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        result = 0
        if b > a:
            a, b = b, a
        for num in range(1, b+1):
            if a % num == 0 and b % num == 0:
                result += 1
        return result
