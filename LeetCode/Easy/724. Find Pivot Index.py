class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_up, sum_down = 0, sum(nums)
        for i in range(len(nums)):
            sum_down -= nums[i]
            if sum_up == sum_down:
                return i
            sum_up += nums[i]
        return -1
