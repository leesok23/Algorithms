class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for word in word1:
            if abs(word1.count(word) - word2.count(word)) > 3:
                return False
        for word in word2:
            if abs(word1.count(word) - word2.count(word)) > 3:
                return False
        return True
