class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}

        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = i
            else:
                if i - dct[nums[i]] <= k:
                    return True
                else:
                    dct[nums[i]] = i
        return False
