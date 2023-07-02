class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        result = []
        for string in s:
            if string == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        
        return result + [high]
