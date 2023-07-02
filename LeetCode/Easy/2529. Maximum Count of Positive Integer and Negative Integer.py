# Version 1
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg, pos = 0, 0
        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1
        return max(neg, pos)


# Version 2
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        i = 0
        neg = len(nums)
        while i < len(nums) and nums[i] <= 0:
            if nums[i] == 0:
                neg = min(neg, i)
            i += 1
        neg = min(neg, i)
        return max(len(nums[:neg]), len(nums[i:]))
