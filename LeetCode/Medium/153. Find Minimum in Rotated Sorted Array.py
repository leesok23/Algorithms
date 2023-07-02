class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        num0 = nums[0]
        for num in nums[1:]:
            if num < num0:
                return num
        return num0
