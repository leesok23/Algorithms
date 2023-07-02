class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def wordInt(word):
            count = ''
            for w in word:
                count += str(ord(w) - ord('a'))
            return int(count)

        return wordInt(firstWord) + wordInt(secondWord) == wordInt(targetWord)
