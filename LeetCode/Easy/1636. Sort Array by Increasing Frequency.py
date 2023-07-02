class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        result = []
        for key, value in sorted(hashmap.items(), key=lambda x: (x[1],x[0]*(-1))):
            result += [key] * value
        return result
