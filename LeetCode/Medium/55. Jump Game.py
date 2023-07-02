class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        leftMostInd = len(nums) - 1
        for i in range(len(nums)-1)[::-1]:
            if nums[i] + i >= leftMostInd:
                leftMostInd = i
        return True if leftMostInd == 0 else False
