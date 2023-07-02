class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        result = ''
        for char in s:
            if char not in vowels:
                result += char
        return result
