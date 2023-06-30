class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        elif s[0] == ' ':
            result = ' '
            j = 1
        else:
            result = ''
            j = 0
            
        for i in range(1, len(s)):
            if s[i] == ' ':
                result = result + s[j:i][::-1] + ' '
                j = i + 1
                
        result = result + s[j:][::-1]
        
        return result
