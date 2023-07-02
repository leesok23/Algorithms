class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_int, num2_int = int(num1), int(num2)
        num_int = num1_int + num2_int
        return str(num_int)
