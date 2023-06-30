class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score_ind = sorted(range(len(score)), key=lambda x: score[x], reverse=True)
        result = [0] * len(score)
        for i in range(len(sorted_score_ind)):
            if i == 0:
                result[sorted_score_ind[i]] = 'Gold Medal'
            elif i == 1:
                result[sorted_score_ind[i]] ='Silver Medal'
            elif i == 2:
                result[sorted_score_ind[i]] = 'Bronze Medal'
            else:
                result[sorted_score_ind[i]] = str(i+1)
        return result
