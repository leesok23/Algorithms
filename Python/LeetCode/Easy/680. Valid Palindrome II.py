class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(left, right, chars):
            while left < right:
                if chars[left] != chars[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return checkPalindrome(l+1, r, s) or checkPalindrome(l, r-1, s)
        
        return True
