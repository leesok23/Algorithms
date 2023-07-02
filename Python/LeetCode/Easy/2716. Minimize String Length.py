class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s_list = []
        count = 0
        for i in range(len(s)):
            if s[i] not in s_list:
                count += 1
                s_list.append(s[i])
        return count
