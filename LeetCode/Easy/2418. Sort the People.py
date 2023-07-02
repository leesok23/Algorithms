class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ind = sorted(range(len(heights)), key=lambda x: heights[x], reverse=True)
        result = []
        for i in ind:
            result.append(names[i])
        return result
