class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        listS = list(s)
        for i in range(len(s))[::2*k]:
            listS[i:i+k] = listS[i:i+k][::-1]
            
        return ''.join(listS)
