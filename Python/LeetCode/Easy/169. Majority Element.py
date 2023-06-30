class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        
        for num in nums:
            if mapping[num] > len(nums)/2:
                return num
