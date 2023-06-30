class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashmap = {}
        for string in s:
            if string not in hashmap:
                hashmap[string] = 1
            else:
                hashmap[string] += 1

        n = 0
        for value in hashmap.values():
            if value % 2 == 1:
                n += 1
                if n > 1:
                    return False
        
        return True
