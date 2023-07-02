class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for l in range(1, len(arr)+1, 2):
            for i in range(len(arr)-l+1):
                result += sum(arr[i:i+l])
        return result
