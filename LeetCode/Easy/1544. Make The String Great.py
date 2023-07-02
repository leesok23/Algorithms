class Solution:
    def makeGood(self, s: str) -> str:
        result = s[0]
        for i in range(1,len(s)):
            if result != '':
                if s[i].isupper() and result[-1].islower() and s[i].lower() == result[-1]:
                    print(s[i])
                    result = result[:-1]
                elif s[i].islower() and result[-1].isupper() and s[i].upper() == result[-1]:
                    print(s[i])
                    result = result[:-1]
                else:
                    result += s[i]
            else:
                result += s[i]
        
        return result
