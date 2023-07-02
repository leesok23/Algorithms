class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            len_word = len(word)
            if word == s[:len_word]:
                count += 1
        return count
