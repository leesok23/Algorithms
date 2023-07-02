class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        for word in words:
            len_word = len(word)
            for i in range(len(text)-len_word+1):
                if word == text[i:i+len_word]:
                    result.append([i,i+len_word-1])
        result.sort()
        return result
