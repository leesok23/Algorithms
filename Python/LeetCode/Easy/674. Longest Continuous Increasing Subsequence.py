class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        n, m = 1, 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                n += 1
            else:
                if n > m:
                    m = n
                n = 1
        if n > m:
            m = n
            
        return m
