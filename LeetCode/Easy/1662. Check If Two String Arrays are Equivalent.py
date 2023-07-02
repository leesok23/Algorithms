# Version 1
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        result1, result2 = '', ''
        for word in word1:
            result1 += word
        for word in word2:
            result2 += word
        return result1 == result2


# Version 2
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
