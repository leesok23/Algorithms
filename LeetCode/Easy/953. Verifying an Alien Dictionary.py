class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            len1 = len(words[i])
            len2 = len(words[i+1])
            n = 0
            while n < len1 and n < len2:
                if order.index(words[i][n]) == order.index(words[i+1][n]):
                    n += 1
                elif order.index(words[i][n]) < order.index(words[i+1][n]):
                    break
                else:
                    return False
            if n < len1 and n >= len2:
                return False
        
        return True
