# Version 1
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[:i]) - sum(nums[i+1:])) for i in range(len(nums))]


# Version 2
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = [], []
        for i in range(len(nums)):
            leftSum.append(sum(nums[:i]))
            rightSum.append(sum(nums[i+1:]))
        result = []
        for i in range(len(leftSum)):
            result.append(abs(leftSum[i]-rightSum[i]))
        return result
