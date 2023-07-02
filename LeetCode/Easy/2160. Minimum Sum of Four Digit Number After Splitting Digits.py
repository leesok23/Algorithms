class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = []
        while num > 0:
            num_list.append(num%10)
            num //= 10
        num_list.sort()
        return (num_list[0]*10+num_list[2]) + (num_list[1]*10+num_list[3])
