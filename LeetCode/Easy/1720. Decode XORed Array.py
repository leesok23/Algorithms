class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for item in encoded:
            temp = item^first
            arr.append(temp)
            first = temp
        return arr
