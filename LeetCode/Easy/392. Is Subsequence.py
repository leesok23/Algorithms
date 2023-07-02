class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        n = 0
        for i in range(len(t)):
            if s[n] == t[i]:
                n += 1
                if n == len(s):
                    return True
        return False
