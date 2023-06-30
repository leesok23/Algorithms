class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list_ransomNote = list(ransomNote)
        for s in magazine:
            if s in list_ransomNote:
                list_ransomNote.remove(s)
        return True if len(list_ransomNote) == 0 else False
