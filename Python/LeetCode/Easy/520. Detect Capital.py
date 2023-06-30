class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        elif word[1:].islower():
            return True
        elif word.isupper():
            return True
        else:
            return False
