class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        for num in nums1:
            if num in nums2:
                intersect.append(num)
                nums2.remove(num)
        
        return intersect
