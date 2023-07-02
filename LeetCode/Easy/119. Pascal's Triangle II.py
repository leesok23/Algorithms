class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for i in range(1,rowIndex+1):
            temp = [0] + result + [0]
            result = []
            for j in range(len(temp)-1):
                result.append(temp[j] + temp[j+1])
        
        return result
