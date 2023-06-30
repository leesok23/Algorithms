class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = 0
        for num in arr:
            if num % 2 == 1:
                n += 1
                if n == 3:
                    return True
            else:
                n = 0
        return False
