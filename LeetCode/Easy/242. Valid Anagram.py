class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dct_s = {}
        dct_t = {}
        
        for i in range(len(s)):
            if s[i] not in dct_s:
                dct_s[s[i]] = 1
            else:
                dct_s[s[i]] += 1
            
            if t[i] not in dct_t:
                dct_t[t[i]] = 1
            else:
                dct_t[t[i]] += 1
        
        return True if dct_s == dct_t else False
