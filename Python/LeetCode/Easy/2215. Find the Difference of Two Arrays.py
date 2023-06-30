# Version 1
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set(nums1)
        num2 = set(nums2)
        return [list(num1-num2), list(num2-num1)]


# Version 2
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = []
        num2 = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in num1:
                num1.append(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] not in nums1 and nums2[j] not in num2:
                num2.append(nums2[j])

        return [num1, num2]
