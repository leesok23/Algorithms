class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(nums[0])):
            n = 0
            for num in nums[1:]:
                if nums[0][i] in num:
                    n += 1
            
            if n == len(nums)-1:
                result.append(nums[0][i])
        
        return sorted(result)
