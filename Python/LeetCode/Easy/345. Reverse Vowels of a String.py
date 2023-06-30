class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ind = {}
        for i in range(len(s)):
            if s[i] in vowels:
                ind[i] = s[i]
        
        n = 0
        listS = list(s)
        indKeys = sorted(ind.keys())
        while n <= len(ind) // 2 and len(ind) > 0:
            i, j = indKeys[n], indKeys[len(ind)-1-n]
            listS[i], listS[j] = ind[j], ind[i]
            n += 1
        return ''.join(listS)
