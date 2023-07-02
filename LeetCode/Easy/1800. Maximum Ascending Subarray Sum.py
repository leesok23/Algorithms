class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        temp = 0
        potential_max = 0
        for i in range(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                temp += nums[i]
            else:
                potential_max = max(potential_max, temp)
                temp = nums[i]
        potential_max = max(potential_max, temp)
        return potential_max
