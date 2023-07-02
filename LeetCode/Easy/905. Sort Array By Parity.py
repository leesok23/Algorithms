class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        prev, curr = 0, 0
        while curr < len(nums):
            if nums[curr] % 2 == 0:
                nums[prev], nums[curr] = nums[curr], nums[prev]
                prev += 1
                curr += 1
            else:
                curr += 1
        return nums
