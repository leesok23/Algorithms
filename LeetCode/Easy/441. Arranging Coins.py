class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left+right) // 2
            temp = mid*(mid+1) // 2
            if temp == n:
                return mid
            elif temp > n:
                right = mid - 1
            else:
                left = mid + 1
        
        return right
