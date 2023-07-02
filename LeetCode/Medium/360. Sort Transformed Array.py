class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        result = []
        for num in nums:
            result.append(a*num**2 + b*num + c)
        result.sort()
        return result
