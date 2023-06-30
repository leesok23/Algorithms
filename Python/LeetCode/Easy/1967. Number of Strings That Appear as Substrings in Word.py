class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = 0
        for pattern in patterns:
            if pattern in word:
                n += 1
        return n
