class Solution:
    def isValid(self, s: str) -> bool:
        a = ['(', ')']
        b = ['{', '}']
        c = ['[', ']']

        stack = []
        for ch in s:
            if ch == a[0]:
                stack.append(a[1])
            elif ch == b[0]:
                stack.append(b[1])
            elif ch == c[0]:
                stack.append(c[1])
            else:
                if len(stack) == 0:
                    return False
                else:
                    prev = stack.pop()
                    if ch != prev:
                        return False
        
        return True if len(stack) == 0 else False
