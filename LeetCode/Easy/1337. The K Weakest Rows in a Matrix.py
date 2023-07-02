class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        for nums in mat:
            result.append(sum(nums))

        sorted_result = sorted(range(len(result)), key=lambda x: result[x])
        return sorted_result[:k]
