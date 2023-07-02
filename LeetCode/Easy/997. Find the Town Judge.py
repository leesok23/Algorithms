class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust1, trust2 = [0]*n, [0]*n

        for i in range(len(trust)):
            trust1[trust[i][0]-1] += 1
            trust2[trust[i][1]-1] += 1
        
        for i in range(len(trust1)):
            if trust1[i] == 0:
                if trust2[i] == n-1:
                    return i+1
                else:
                    return -1
        return -1
