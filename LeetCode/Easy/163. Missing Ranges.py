class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def addRange(left, right):
            if left == right-1:
                ranges.append(str(left))
            else:
                ranges.append("{}->{}".format(left,right-1))

        ranges = []
        begin = lower
        for num in nums:
            if begin < num:
                addRange(begin, num)
            begin = num + 1
        
        if begin <= upper:
            addRange(begin, upper+1)
        
        return ranges
