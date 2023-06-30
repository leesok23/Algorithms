class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) <= 1:
            return people
        
        result = []
        orderedPeople = sorted(people, key = lambda (h, k): (-h, k))
        for person in orderedPeople:
            result.insert(person[1], person)
        
        return result
