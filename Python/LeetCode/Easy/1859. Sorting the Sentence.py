class Solution:
    def sortSentence(self, s: str) -> str:
        new_s = s.split()
        result = [' '] * len(new_s)
        for string in new_s:
            ind = int(string[-1])
            result[ind-1] = string[:-1]
        return ' '.join(result)
