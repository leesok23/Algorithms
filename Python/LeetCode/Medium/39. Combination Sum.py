class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        def dfs(remaining, i, stack):
            if remaining == 0:
                result.append(stack)
                return
            for j in range(i, len(candidates)):
                if candidates[j] > remaining:
                    break
                else:
                    dfs(remaining - candidates[j], j, stack + [candidates[j]])
        dfs(target, 0, [])
        return result
