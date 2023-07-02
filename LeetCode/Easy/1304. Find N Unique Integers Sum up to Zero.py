class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        elif n % 2 == 1:
            return [0] + list(range(1,n//2+1)) + list(range(-n//2+1,0))
        else:
            return list(range(1,n//2+1)) + list(range(-n//2,0))
