# Version 1
class Solution:
    def sortString(self, s: str) -> str:
        Dict = {}
        for letter in s:
            if letter not in Dict:
                Dict[letter] = 1
            else:
                Dict[letter] += 1
        
        s_keys = sorted(list(Dict.keys()))
        result = ''
        while len(result) != len(s):
            for letter in s_keys:
                if Dict[letter] > 0:
                    result += letter
                    Dict[letter] -= 1
            for letter in s_keys[::-1]:
                if Dict[letter] > 0:
                    result += letter
                    Dict[letter] -= 1
        return result


# Version 2
class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        result = ''
        while len(s) > 0:
            for letter in sorted(set(s)):
                result += letter
                s.remove(letter)
            for letter in sorted(set(s), reverse=True):
                result += letter
                s.remove(letter)
        return result
