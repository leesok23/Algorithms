class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ''
        for i in range(1, len(s), 2):
            result += s[i-1] + chr(ord(s[i-1])+int(s[i]))
        return result if len(s) % 2 == 0 else result + s[-1]
