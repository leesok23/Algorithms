class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n, nR, nL = 0, 0, 0
        for i in range(len(s)):
            if s[i] == 'R':
                nR += 1
            else:
                nL += 1
            if nR == nL:
                n += 1
                nR = 0
                nL = 0
        
        return n
