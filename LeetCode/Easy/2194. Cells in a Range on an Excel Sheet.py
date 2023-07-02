class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        columns = [chr(i) for i in range(ord(s[0]), ord(s[-2])+1)]
        rows = [str(i) for i in range(int(s[1]), int(s[-1])+1)]
        result = []
        for col in columns:
            for row in rows:
                result.append(col+row)
        return result
