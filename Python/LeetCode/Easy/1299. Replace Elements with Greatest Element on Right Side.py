class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1]
        temp = -1
        for i in range(1,len(arr))[::-1]:
            if arr[i] > temp:
                temp = arr[i]
            result.append(temp)
        return result[::-1]
