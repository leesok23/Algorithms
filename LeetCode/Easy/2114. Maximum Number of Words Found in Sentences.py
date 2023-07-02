class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_potential = 0
        for i in range(len(sentences)):
            max_potential = max(max_potential, len(sentences[i].split(' ')))
        return max_potential
