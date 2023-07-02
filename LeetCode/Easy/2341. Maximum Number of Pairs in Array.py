class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pair, leftover = 0, 0
        while len(nums) > 0:
            num = nums.pop(0)
            if num in nums:
                nums.remove(num)
                pair += 1
            else:
                leftover += 1
        return [pair, leftover]
