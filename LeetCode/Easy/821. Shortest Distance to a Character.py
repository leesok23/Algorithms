class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_pos = []
        for i in range(len(s)):
            if s[i] == c:
                c_pos.append(i)

        result = []
        for i in range(len(s)):
            diff = len(s)
            for j in range(len(c_pos)):
                if abs(i-c_pos[j]) < diff:
                    diff = abs(i-c_pos[j])
            result.append(diff)
        return result
