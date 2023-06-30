class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        dct_pattern = {}
        dct_words = {}
        for i in range(len(pattern)):
            if pattern[i] in dct_pattern and dct_pattern[pattern[i]] != words[i]:
                return False
            if words[i] in dct_words and dct_words[words[i]] != pattern[i]:
                return False
            else:
                dct_pattern[pattern[i]] = words[i]
                dct_words[words[i]] = pattern[i]
        
        return True
