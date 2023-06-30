class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            ind = 0
        elif ruleKey == 'color':
            ind = 1
        else:
            ind = 2
        
        count = 0
        for i in range(len(items)):
            if items[i][ind] == ruleValue:
                count += 1
        return count
