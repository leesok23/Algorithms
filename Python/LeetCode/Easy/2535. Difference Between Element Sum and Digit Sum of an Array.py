# Version 1
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            while num > 0:
                digit_sum += num % 10
                num //= 10
        
        return abs(element_sum - digit_sum)


# Version 2
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            if num < 10:
                digit_sum += num
            else:
                str_num = str(num)
                for string in str_num:
                    digit_sum += int(string)
        
        return abs(element_sum - digit_sum)
