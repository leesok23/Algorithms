class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_seen = {}
        count = 0
        for num in nums:
            if num not in num_seen:
                num_seen[num] = 1
                count += num
            else:
                if num_seen[num] == 1:
                    count -= num
                num_seen[num] += 1
        return count
