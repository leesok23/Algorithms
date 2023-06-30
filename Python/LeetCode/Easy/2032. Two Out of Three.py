class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        
        result = []
        for key, value in dict.items():
            if value > 1:
                result.append(key)
        return result
