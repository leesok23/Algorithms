class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        max_prod, min_prod, cur_prod = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
                
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            cur_prod = max(cur_prod, max_prod)
            
        return cur_prod
