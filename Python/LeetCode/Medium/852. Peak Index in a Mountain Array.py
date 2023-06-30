class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = 0
        while arr[n] < arr[n+1]:
            n += 1
        return n
