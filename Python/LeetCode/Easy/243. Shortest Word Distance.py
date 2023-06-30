class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_distance = len(wordsDict)-1
        ind1, ind2 = -1, -1
        for i, word in enumerate(wordsDict):
            if word == word1:
                ind1 = i
            if word == word2:
                ind2 = i
            if ind1 != -1 and ind2 != -1:
                min_distance = min(min_distance, abs(ind1-ind2))
        return min_distance
