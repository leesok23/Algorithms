class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        begin = lower
        result = []

        def addRange(left, right):
            if left == right-1:
                result.append(str(left))
            else:
                result.append("{}->{}".format(left,right-1))
        
        for num in nums:
            if begin < num:
                addRange(begin,num)
            begin = num + 1
        
        if begin <= upper:
            addRange(begin,upper+1)
        
        return result
