class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ind = nums.index(max(nums))
        result = 0
        for i in range(0,len(nums)):
            if i != ind and nums[ind] < nums[i]*2:
                return -1
        return ind
