class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sumInd = len(list1) + len(list2)
        result = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j <= sumInd:
                        result.append(list1[i])
                        sumInd = i + j
        return result
