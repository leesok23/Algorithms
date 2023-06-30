class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count, prev, cur = 0, 0, 1
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                cur += 1
            else:
                count += min(prev, cur)
                prev = cur
                cur = 1
        return count + min(prev, cur)
