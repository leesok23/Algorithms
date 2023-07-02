class Solution:
    def freqAlphabets(self, s: str) -> str:
        temp = ''
        i = len(s)-1
        while i >= 0:
            if s[i] != '#':
                temp += chr(int(s[i])+ord('a')-1)
                i -= 1
            else:
                temp += chr(int(s[i-2:i])+ord('a')-1)
                i -= 3
        return temp[::-1]
