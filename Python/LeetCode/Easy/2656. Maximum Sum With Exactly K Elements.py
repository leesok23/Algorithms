class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0
        nums.sort()
        for i in range(k):
            score += nums[-1]
            nums[-1] += 1
        return score
