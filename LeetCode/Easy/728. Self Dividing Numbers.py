class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):
            list_num = list(str(num))
            TF = True
            for n in list_num:
                if n == '0' or num % int(n) != 0:
                    TF = False
                    break
            if TF:
                result.append(num)
        return result
