class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
        
        for key in dct:
            if dct[key] == 1:
                return key
