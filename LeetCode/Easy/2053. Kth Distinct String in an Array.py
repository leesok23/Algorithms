class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        Dict = {}
        for a in arr:
            if a not in Dict:
                Dict[a] = 1
            else:
                Dict[a] += 1
        n = 0
        for key, value in Dict.items():
            if value == 1:
                n += 1
                if n == k:
                    return key
        return ''
