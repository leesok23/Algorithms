class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        mapping = {}
        for item in items:
            if item[0] not in mapping:
                mapping[item[0]] = [item[1]]
            else:
                if len(mapping[item[0]]) < 5:
                    mapping[item[0]].append(item[1])
                else:
                    if min(mapping[item[0]]) < item[1]:
                        mapping[item[0]].append(item[1])
                        ind = mapping[item[0]].index(min(mapping[item[0]]))
                        mapping[item[0]].pop(ind)
        
        result = []
        for key, value in mapping.items():
            result.append([key, sum(value)//5])
    
        return result
