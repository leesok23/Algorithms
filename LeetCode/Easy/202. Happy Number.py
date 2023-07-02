class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        
        list_n = []
        while True:
            temp_result = (n%10)**2
            while n//10 != 0:
                n = n//10
                temp_result += (n%10)**2
            n = temp_result
            if n == 1:
                return True
            if n not in list_n:
                list_n.append(n)
                
            else:
                return False
