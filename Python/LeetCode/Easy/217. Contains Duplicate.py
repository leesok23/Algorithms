class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                return True
        return False
