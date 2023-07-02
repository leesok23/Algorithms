class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        num = 0
        for i in range(len(nums)):
            num += nums[i]
            result.append(num)
        return result
