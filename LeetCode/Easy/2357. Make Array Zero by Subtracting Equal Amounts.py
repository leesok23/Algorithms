class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1 and nums[0] != 0:
            return 1
        
        n = 0
        diff = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                n += 1
                diff += nums[i+1] - nums[i]
        
        if diff < nums[-1]:
            n += 1
    
        return n
