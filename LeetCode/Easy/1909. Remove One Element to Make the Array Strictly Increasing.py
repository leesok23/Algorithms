class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def increasing(sub_nums):
            for i in range(len(sub_nums)-1):
                if sub_nums[i] >= sub_nums[i+1]:
                    return False
            return True
        
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return increasing(nums[:i]+nums[i+1:]) or increasing(nums[:i+1]+nums[i+2:])
        return True
