class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = []
        for char in words[0]:
            n = 0
            for i in range(1,len(words)):
                if char in words[i]:
                    n += 1

            if n == len(words)-1:
                common.append(char)
                for i in range(1,len(words)):
                    ind = words[i].index(char)
                    words[i] = words[i][:ind] + words[i][ind+1:]
        
        return common
