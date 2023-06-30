class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in dct:
                return [dct[remaining], i]
            else:
                dct[nums[i]] = i
