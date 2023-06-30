class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dctS = {}
        dctT = {}
        
        for ind in s:
            if ind not in dctS:
                dctS[ind] = 1
            else:
                dctS[ind] += 1
        for ind in t:
            if ind not in dctT:
                dctT[ind] = 1
            else:
                dctT[ind] += 1
            
        for key in dctT:
            if key not in dctS or dctT[key] != dctS[key]:
                return key
