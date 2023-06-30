# Version 1
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        return [sorted_nums.index(i) for i in nums]


# Version 2
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[j] < nums[i]:
                    temp += 1
            result.append(temp)
        return result
