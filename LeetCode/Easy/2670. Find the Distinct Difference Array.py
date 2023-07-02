class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prefix = len(set(nums[:i+1]))
            suffix = len(set(nums[i+1:]))
            result.append(prefix-suffix)
        return result
