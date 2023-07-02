class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dct = {}
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
        return sorted(dct.keys(), key = lambda x: dct[x], reverse=True)[:k]
