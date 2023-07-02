class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = min(nums)
        result = 0
        while min_num > 0:
            result += min_num % 10
            min_num //= 10
        return 0 if result % 2 == 1 else 1
