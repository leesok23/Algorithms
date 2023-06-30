class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret_dict = {}
        for i in range(max(len(items1), len(items2))):
            if i < len(items1):
                if items1[i][0] not in ret_dict:
                    ret_dict[items1[i][0]] = items1[i][1]
                else:
                    ret_dict[items1[i][0]] += items1[i][1]
            if i < len(items2):
                if items2[i][0] not in ret_dict:
                    ret_dict[items2[i][0]] = items2[i][1]
                else:
                    ret_dict[items2[i][0]] += items2[i][1]
        ret = []
        for key, value in ret_dict.items():
            ret.append([key, value])
        return sorted(ret)
