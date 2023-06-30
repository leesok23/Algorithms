class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        count_num = {}
        for num in nums:
            if num not in count_num:
                count_num[num] = 1
            else:
                count_num[num] += 1
                if count_num[num] == n:
                    return num
