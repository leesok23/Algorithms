class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dict = {key: value for value, key in enumerate(keyboard)}
        cur = 0
        n = 0
        for w in word:
            past = cur
            cur = dict[w]
            n += abs(cur - past)
        return n
