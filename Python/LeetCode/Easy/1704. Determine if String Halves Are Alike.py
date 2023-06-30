class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = ['a','e','i','o','u']
        mid = len(s) // 2
        
        count1 = sum([ch in vowels for ch in s[:mid]])
        count2 = sum([ch in vowels for ch in s[mid:]])
        
        return True if count1 == count2 else False
