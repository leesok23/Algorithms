class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            result.append(-1)
            index1 = nums2.index(num)
            index2 = len(result)-1
            for i in range(index1,len(nums2)-1):
                if nums2[i+1] > nums2[index1]:
                    result[index2] = nums2[i+1]
                    break
        
        return result
