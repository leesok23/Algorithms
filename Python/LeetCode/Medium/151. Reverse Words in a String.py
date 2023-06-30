class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        result = []
        for i in range(len(words))[::-1]:
            if words[i] != '':
                result.append(words[i])
        words = ' '.join(result)
                
        return words
