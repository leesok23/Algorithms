class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = []
        for i in range(len(queries)):
            count = 0
            for j in range(len(nums)):
                count += nums[j]
                if count > queries[i]:
                    result.append(j)
                    break
                elif j == len(nums)-1:
                    result.append(j+1)
                    break
        return result
