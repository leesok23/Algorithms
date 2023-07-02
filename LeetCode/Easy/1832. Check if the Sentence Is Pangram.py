class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        result = [0 for i in range(ord('a'), ord('z')+1)]
        for char in sentence:
            index = ord(char) - ord('a')
            result[index] += 1
        
        return False if result.count(0) > 0 else True
