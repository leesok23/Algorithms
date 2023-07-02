# Version 1
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s_list = s.split()
        return ' '.join(s_list[:k])


# Version 2
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        n = 0
        for i in range(len(s)):
            if s[i] == " ":
                n += 1
            if n == k:
                return s[:i]
        return s
