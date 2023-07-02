class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(0, len(nums)-2):
            temp = nums[i]
            n = 1
            for j in range(i+1, len(nums)):
                if nums[j]-temp == diff:
                    temp = nums[j]
                    n += 1
                if n == 3:
                    count += 1
                    break
        return count
