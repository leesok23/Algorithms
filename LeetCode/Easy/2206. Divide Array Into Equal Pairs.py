class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        for key, value in dict.items():
            if value % 2 != 0:
                return False
        return True
