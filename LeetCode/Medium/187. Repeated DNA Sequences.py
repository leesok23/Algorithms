class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dct = {}
        for i in range(len(s)-9):
            if s[i:i+10] not in dct:
                dct[s[i:i+10]] = 1
            else:
                dct[s[i:i+10]] += 1
        res = []
        for key in dct:
            if dct[key] > 1:
                res.append(key)
        return res
