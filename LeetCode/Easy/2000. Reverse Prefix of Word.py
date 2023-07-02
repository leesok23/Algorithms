class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        ind_ch = word.index(ch)
        return word[:ind_ch+1][::-1] + word[ind_ch+1:]
