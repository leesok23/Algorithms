class Solution:
    def minTimeToType(self, word: str) -> int:
        count = len(word) + min(ord(word[0])-ord('a'), ord('z')+1-ord(word[0]))
        for i in range(1,len(word)):
            a = min(ord(word[i]), ord(word[i-1]))
            b = max(ord(word[i]), ord(word[i-1]))
            count += min(b-a, ord('z')-ord('a')+1+a-b)
        return count
