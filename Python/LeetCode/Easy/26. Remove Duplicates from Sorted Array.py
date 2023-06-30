class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        pos = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pos]:
                pos += 1
                nums[i], nums[pos] = nums[pos], nums[i]
        return pos + 1
