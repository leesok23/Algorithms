class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = 0
        for i in range(len(seats)):
            n += abs(seats[i]-students[i])
        return n
