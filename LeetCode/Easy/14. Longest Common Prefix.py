class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for i in range(len(strs[0])):
            n = 0
            for j in range(1,len(strs)):
                if len(strs[j]) <= i:
                    return result

                if strs[0][i] == strs[j][i]:
                    n += 1
                else:
                    return result
            
            if n == len(strs)-1:
                result += strs[0][i]
        
        return result
