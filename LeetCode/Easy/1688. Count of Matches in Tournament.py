class Solution:
    def numberOfMatches(self, n: int) -> int:
        match = 0
        while n > 1:
            match += n // 2
            if n % 2 == 0:
                n = n // 2
            else:
                n = n // 2 + 1
        return match
