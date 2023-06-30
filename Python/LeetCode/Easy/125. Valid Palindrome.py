class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in range(len(s)):
            if s[i].isalnum():
                s_lower = s[i].lower()
                string.append(s_lower)
        
        left, right = 0, len(string)-1
        while left < right:
            if string[left] != string[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
