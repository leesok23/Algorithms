class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)
        for num in nums:
            if num < target:
                left += 1
            elif num > target:
                right -= 1
        return list(range(left, right))
