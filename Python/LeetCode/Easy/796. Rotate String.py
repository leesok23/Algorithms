class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        elif len(A) == 0 and len(B) == 0:
            return True
        
        n = 0
        for i in range(len(A)):
            AA = A[i:] + A[:i]
            if AA == B:
                n += 1
                
        return True if n > 0 else False
