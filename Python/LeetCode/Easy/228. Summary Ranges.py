class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        begin = 0
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] != nums[i+1]-1:
                if i == begin:
                    result.append(str(nums[i]))
                    begin = i + 1
                else:
                    result.append(str(nums[begin])+"->"+str(nums[i]))
                    begin = i + 1
            
            if i == len(nums)-1:
                if nums[i] == nums[i-1]+1:
                    result.append(str(nums[begin])+"->"+str(nums[i]))
                else:
                    result.append(str(nums[i]))
        
        return result
