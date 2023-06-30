# Version 1
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        result = []
        count1, count2 = 0, sum(nums)
        i = 0
        while i < len(nums):
            count1 += nums[i]
            count2 -= nums[i]
            result.append(nums[i])
            i += 1
            if count1 > count2:
                return result


# Version 2
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        for i in range(1,len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
        return nums
