class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        temp = ''
        counter = 0
        for i in s:
            if i == '(':
                counter += 1
            else:
                counter -= 1
            
            temp += i
            if counter == 0:
                result += temp[1:-1]
                temp = ''
    
        return result
