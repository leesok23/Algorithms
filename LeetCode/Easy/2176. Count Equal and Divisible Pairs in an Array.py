class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0
        dictionary = defaultdict(list)
        for i in range(len(nums)):
            for j in dictionary[nums[i]]:
                if (i*j)%k == 0:
                    result += 1
            dictionary[nums[i]].append(i)
        return result
