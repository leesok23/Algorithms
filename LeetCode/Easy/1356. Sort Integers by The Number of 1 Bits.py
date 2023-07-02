# Version 1
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key=lambda x: bin(x).count('1'))


# Version 2
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        n = max(arr)
        count = [0]
        for i in range(1, n+1):
            count.append(count[i//2] + (i%2))

        count_arr = []
        for num in arr:
            count_arr.append(count[num])

        return sorted(arr, key=lambda x: count_arr[arr.index(x)])
