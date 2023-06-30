class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        i = 0
        tot = 0
        while truckSize > 0 and i < len(boxTypes):
            if boxTypes[i][0] <= truckSize:
                tot += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                tot += truckSize * boxTypes[i][1]
                truckSize = 0
            i += 1
        return tot
