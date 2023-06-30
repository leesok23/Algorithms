class Solution:
    def repeatedCharacter(self, s: str) -> str:
        new_s = ''
        for string in s:
            if string in new_s:
                return string
            new_s += string
