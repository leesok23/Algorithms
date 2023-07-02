class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        
        result = [[]]
        for num in nums:
            temp = []
            for item in result:
                temp.append(item + [num])
                temp.append(item)
            result = temp
            
        return result
