class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        character = ord(coordinates[0]) - ord('a') + 1
        number = int(coordinates[1])
        if (character+number) % 2 == 0:
            return False
        else:
            return True
