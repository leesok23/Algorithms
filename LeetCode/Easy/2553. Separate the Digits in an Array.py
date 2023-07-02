class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            temp = [int(x) for x in str(num)]
            result += temp
        return result
