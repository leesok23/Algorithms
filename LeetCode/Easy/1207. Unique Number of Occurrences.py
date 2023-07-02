class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = {}

        for num in arr:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
        
        freq = []
        for value in dct.values():
            if value in freq:
                return False
            else:
                freq.append(value)
        
        return True
