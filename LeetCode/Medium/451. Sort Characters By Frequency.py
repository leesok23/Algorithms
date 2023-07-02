class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dct = {}
        for ch in s:
            if ch not in dct:
                dct[ch] = 1
            else:
                dct[ch] += 1
        
        sortDct = sorted(dct.keys(), key = lambda x: dct[x], reverse = True)
        res = ''
        for ch in sortDct:
            res += ch * dct[ch]
        return res
