class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dct = {}
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = 1
            else:
                dct[nums[i]] += 1
                
        result = []
        for key in dct:
            if dct[key] == 1:
                result += [key]
        return result
