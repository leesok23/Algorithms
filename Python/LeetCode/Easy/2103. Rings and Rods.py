class Solution:
    def countPoints(self, rings: str) -> int:
        result = {}
        for i in range(1, len(rings), 2):
            if rings[i] not in result:
                result[rings[i]] = [rings[i-1]]
            elif rings[i] in result and rings[i-1] not in result[rings[i]]:
                result[rings[i]].append(rings[i-1])
        
        count = 0
        for value in result.values():
            if len(value) == 3:
                count += 1
        return count
