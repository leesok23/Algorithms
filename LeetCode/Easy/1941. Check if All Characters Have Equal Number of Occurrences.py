class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        Dict = {}
        for string in s:
            if string not in Dict:
                Dict[string] = 1
            else:
                Dict[string] += 1
        result = [value for value in Dict.values()]
        for i in range(1,len(result)):
            if result[i] != result[i-1]:
                return False
        return True
