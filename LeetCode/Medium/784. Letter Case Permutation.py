class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = ['']
        for ch in S:
            temp = []
            if not ch.isdigit():
                for string in result:
                    temp.append(string + ch.lower())
                    temp.append(string + ch.upper())
            else:
                for string in result:
                    temp.append(string + ch)
            result = temp
        
        return result
