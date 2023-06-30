class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        pos = 0
        for ch in columnTitle[::-1]:
            digit = ord(ch) - ord("A") + 1
            result += digit * (ord("Z")-ord("A")+1)**pos
            pos += 1
        return result
