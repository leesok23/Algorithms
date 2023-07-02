class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        diff = arr[-1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] > diff:
                continue

            if arr[i+1] - arr[i] < diff:
                result = []
                diff = arr[i+1] - arr[i]
            
            result.append([arr[i],arr[i+1]])
        
        return result
