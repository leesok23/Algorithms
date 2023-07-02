# Version 1
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# Version 2
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
            
        current = 0
        prev1, prev2 = 0, 1
        for i in range(2, n+1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current
