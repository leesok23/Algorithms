class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []
        i, j, k = 0, 0, 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                max_arr = max(arr1[i], arr2[j], arr3[k])
                if arr1[i] < max_arr:
                    i += 1
                elif arr2[j] < max_arr:
                    j += 1
                elif arr3[k] < max_arr:
                    k += 1
        
        return result
