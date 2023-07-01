class Solution:
    def pivotInteger(self, n: int) -> int:
        list_integer = list(range(1, n+1))
        for i in range(len(list_integer)):
            if sum(list_integer[:i+1]) == sum(list_integer[i:]):
                return i + 1
        return -1
