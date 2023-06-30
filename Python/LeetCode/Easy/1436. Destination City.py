class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations = [path[1] for path in paths]
        departures = [path[0] for path in paths]
        for destination in set(destinations):
            if destination not in departures:
                return destination
