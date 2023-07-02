class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return - 1
        elif len(s) == 1:
            return 0
        
        dct = {}
        for ch in s:
            if ch not in dct:
                dct[ch] = 1
            else:
                dct[ch] += 1
        result = []
        for key in dct:
            if dct[key] == 1:
                result.append(s.index(key))
                
        return min(result) if len(result) > 0 else -1
