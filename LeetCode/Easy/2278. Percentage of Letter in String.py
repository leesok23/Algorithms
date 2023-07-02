class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count_letter = 0
        for string in s:
            if string == letter:
                count_letter += 1
        return floor(count_letter / len(s) * 100)
