class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
                if len(hashmap) == 3:
                    return num
        return nums[0]
