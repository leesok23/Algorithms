class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cumsum, startValue = 0, 1
        for num in nums:
            cumsum += num
            if cumsum < 1:
                startValue = max(startValue, 1-cumsum)
        return startValue
