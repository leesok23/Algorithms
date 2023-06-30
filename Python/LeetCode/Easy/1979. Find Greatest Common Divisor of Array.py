class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        n = min(nums)
        while n > 1:
            if min_num % n == 0 and max_num % n == 0:
                return n
            n -= 1
        return 1
