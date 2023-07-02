class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dct = {}
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
        res = []
        for key in dct:
            if dct[key] == 2:
                res.append(key)
        return res
