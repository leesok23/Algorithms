class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dct_s = {}
        dct_t = {}
        for i in range(len(s)):
            if s[i] in dct_s and dct_s[s[i]] != t[i]:
                return False
            elif t[i] in dct_t and dct_t[t[i]] != s[i]:
                return False
            else:
                dct_s[s[i]] = t[i]
                dct_t[t[i]] = s[i]
        
        return True
