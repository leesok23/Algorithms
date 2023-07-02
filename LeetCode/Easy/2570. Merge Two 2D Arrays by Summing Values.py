class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums = nums1 + nums2
        nums.sort()
        Dict = {}
        for num in nums:
            if num[0] not in Dict:
                Dict[num[0]] = num[1]
            else:
                Dict[num[0]] += num[1]
        result = [[key, value] for key, value in Dict.items()]
        return result
