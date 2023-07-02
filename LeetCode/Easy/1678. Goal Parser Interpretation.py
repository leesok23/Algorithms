# Version 1
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace('()', 'o').replace('(al)', 'al')


# Version 2
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        result = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                result += command[i]
                i += 1
            elif command[i:i+2] == '()':
                result += 'o'
                i += 2
            elif command[i:i+2] == '(a':
                result += 'al'
                i += 4
        return result
