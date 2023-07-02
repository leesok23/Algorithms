class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for op in operations:
            if op == 'D':
                val = result[-1] * 2
                result.append(val)
            elif op == 'C':
                result.pop()
            elif op == '+':
                val = result[-1] + result[-2]
                result.append(val)
            else:
                result.append(int(op))
        return sum(result)
