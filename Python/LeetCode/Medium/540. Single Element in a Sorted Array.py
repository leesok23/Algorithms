class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while (l < r):
            m = (l+r) // 2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            elif (m%2==0 and nums[m]==nums[m-1]) or (m%2!=0 and nums[m]!=nums[m-1]):
                r = m-1
            else:
                l = m+1
        return nums[r]
