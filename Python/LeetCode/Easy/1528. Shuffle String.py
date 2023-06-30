class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = [0] * len(s)
        for i, ind in enumerate(indices):
            temp[ind] = s[i]
        return ''.join(temp)
