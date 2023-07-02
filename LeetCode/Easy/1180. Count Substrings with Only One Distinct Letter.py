class Solution:
    def countLetters(self, s: str) -> int:
        total, left = 0, 0
        for right in range(1, len(s)+1):
            if right == len(s) or s[left] != s[right]:
                len_substring = right - left
                total += len_substring * (len_substring+1) // 2
                left = right
        return total
