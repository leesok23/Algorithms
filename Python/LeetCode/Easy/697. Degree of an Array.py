class Solution(object):
    def findShortestSubArray(self, nums):
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
        
        maxDct = max(dct.values())
        degree = [key for key in dct if dct[key] == maxDct]
        result = []
        for d in degree:
            s = nums.index(d)
            f = 1
            distance = 1
            while f < maxDct:
                if nums[s+distance] == d:
                    f += 1
                distance += 1
            result.append(distance)
            
        return min(result)
