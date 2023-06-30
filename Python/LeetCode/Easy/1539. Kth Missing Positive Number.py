class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        for num in range(1,arr[-1]+k+1):
            if num not in arr:
                count += 1
            if count == k:
                return num
