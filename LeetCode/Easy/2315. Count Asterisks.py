class Solution:
    def countAsterisks(self, s: str) -> int:
        n = 0
        result = 0
        for i in range(len(s)):
            if s[i] == '|':
                n += 1
            if n % 2 == 0 and s[i] == '*':
                result += 1
        return result
