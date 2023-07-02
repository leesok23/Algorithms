# Version 1
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palindrome(word):
            left, right = 0, len(word)-1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if palindrome(word):
                return word
        return ''


# Version 2
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ''
