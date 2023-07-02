class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x
        while left <= right:
            mid = (left+right) // 2
            if mid**2 <= x and (mid+1)**2 > x:
                return mid
            elif (mid+1)**2 <= x:
                left = mid + 1
            else:
                right = mid - 1
        
        return mid
