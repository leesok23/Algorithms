class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(n):
            j = i + 1
            if j % 3 == 0 and j % 5 == 0:
                result.append('FizzBuzz')
            elif j % 3 == 0:
                result.append('Fizz')
            elif j % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(j))

        return result
