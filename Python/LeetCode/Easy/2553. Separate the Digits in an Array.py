class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = ''
        for num in nums:
            result += str(num)
        return [int(x) for x in result]
