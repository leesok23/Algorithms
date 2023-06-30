class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        short_len = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(short_len):
            result += word1[i] + word2[i]
        return result + word1[short_len:] + word2[short_len:]
