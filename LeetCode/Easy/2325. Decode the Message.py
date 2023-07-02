class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_letters = []
        for letter in key:
            if letter != ' ' and letter not in key_letters:
                key_letters.append(letter)
        result = ''
        for word in message:
            if word != ' ':
                result += chr(ord('a')+key_letters.index(word))
            else:
                result += ' '
        return result
