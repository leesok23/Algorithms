class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.",
        "....","..",".---","-.-",".-..","--","-.","---",".--.",
        "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        hashmap = {}
        for word in words:
            temp = ''
            for i in range(len(word)):
                ind = ord(word[i]) - ord('a')
                temp += morse[ind]
            if temp not in hashmap:
                hashmap[temp] = 1
        
        return len(hashmap)
